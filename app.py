from flask import Flask, request, render_template_string
from langgraph.graph import StateGraph, END
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFacePipeline
from langchain_core.documents import Document
from transformers import pipeline

# Flask App
app = Flask(__name__)

# Custom FAQ Loader to Split Q&A Pairs
def load_faq(file_path):
    with open(file_path, "r") as f:
        content = f.read().strip().split("\n\n")
    documents = []
    for entry in content:
        if "Q:" in entry and "A:" in entry:
            question = entry.split("A:")[0].replace("Q:", "").strip()
            answer = entry.split("A:")[1].strip()
            documents.append(Document(page_content=f"Q: {question}\nA: {answer}"))
    return documents

# Setup Knowledge Base (FAQ)
faq_documents = load_faq("faq.txt")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store = FAISS.from_documents(faq_documents, embeddings)

# Setup LLM (optional for now)
pipe = pipeline("text-generation", model="distilgpt2", max_length=100)
llm = HuggingFacePipeline(pipeline=pipe)

# Define State and Workflow
class State(dict):
    query: str
    retrieved: str
    response: str
    escalate: bool

def greet(state):
    state["response"] = "Hello! How can I assist you today?"
    return state

def retrieve(state):
    docs = vector_store.similarity_search_with_score(state["query"], k=1)
    doc, distance = docs[0] if docs else (None, float('inf'))
    print(f"Query: {state['query']}")
    print(f"Retrieved: {doc.page_content if doc else 'None'} (Distance: {distance})")
    if doc and distance < 1.0:  # Lower distance = better match; threshold tuned to 1.0
        retrieved_text = doc.page_content
        state["retrieved"] = retrieved_text.split("A:")[1].strip()
    else:
        state["retrieved"] = "No info found."
    print(f"Selected: {state['retrieved']}")
    return state

def respond(state):
    if "urgent" in state["query"].lower():
        state["response"] = "I don’t have specific info for urgent requests."
        state["escalate"] = True
    elif "No info found" not in state["retrieved"]:
        state["response"] = f"You can {state['retrieved'].lower()}."
    else:
        state["response"] = "I don’t have that information."
        state["escalate"] = True
    return state

def escalate_query(state):
    if state["escalate"]:
        state["response"] += "\nI’m sorry, I can’t assist further. Escalating to a human agent."
    return state

workflow = StateGraph(State)
workflow.add_node("greet", greet)
workflow.add_node("retrieve", retrieve)
workflow.add_node("respond", respond)
workflow.add_node("escalate_query", escalate_query)
workflow.set_entry_point("greet")
workflow.add_edge("greet", "retrieve")
workflow.add_edge("retrieve", "respond")
workflow.add_edge("respond", "escalate_query")
workflow.add_edge("escalate_query", END)
graph_app = workflow.compile()

# Flask Routes
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>Customer Support Simulator</title></head>
<body>
    <h1>Customer Support Simulator</h1>
    <div style="border: 1px solid #ccc; padding: 10px; height: 300px; overflow-y: scroll;">
        {% if response %}
            <p><b>Agent:</b> {{ response }}</p>
        {% endif %}
    </div>
    <form method="POST">
        <label>Your Query:</label><br>
        <input type="text" name="query" style="width: 300px;"><br><br>
        <input type="submit" value="Send">
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    response = None
    if request.method == "POST":
        query = request.form.get("query", "")
        if query:
            state = {"query": query, "retrieved": "", "response": "", "escalate": False}
            result = graph_app.invoke(state)
            response = result["response"]
    return render_template_string(HTML_TEMPLATE, response=response)

if __name__ == "__main__":
    app.run(debug=True)