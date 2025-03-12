# AI Customer Support Agent - LangChain, LangGraph, RAG, LLM, Agentic AI 🤖✨

Welcome to the **AI Customer Support Agent**—your friendly, Flask-powered chatbot built with LangChain, FAISS, and LangGraph! 🎉 This Week 1 version is the foundation of an epic customer support simulator that answers FAQs, escalates urgent queries, and sets the stage for more awesomeness to come. Built for my CMPE 273 class at SJSU, this project is all about blending AI smarts with a slick local setup. Let’s dive in! 🚀

## What’s This All About? 🌈
This is a local web app that:
- 🚚 **Retrieves answers** from an FAQ file using RAG (Retrieval-Augmented Generation).
- 🧠 **Thinks** with a simple LLM (distilgpt2 for now—more brains later!).
- 🛠️ **Orchestrates** workflows with LangGraph.
- 🌐 **Serves** it all via Flask on `http://127.0.0.1:5000/`.

Week 1 nails the basics: ask it stuff, get answers, or get escalated if it’s clueless or urgent! 😎

---

## Features 🎯
- **FAQ Lookup**: Ask about tracking, returns, or support contacts—it’s got you! 📦📧
- **Smart Escalation**: Say "urgent" or stump it, and it’ll call for human backup! 🆘
- **Simple UI**: A chat box that’s ready to grow into something fancier. 💬

---

## Tech Stack 🛠️
- **Python 3.12** 🐍: The backbone of our AI buddy.
- **Flask** 🌐: Lightweight web server magic.
- **LangChain** 🔗: Powers RAG for FAQ smarts.
- **FAISS** 📚: Vector store for fast FAQ lookups.
- **LangGraph** 📈: Workflow orchestration FTW!
- **Hugging Face Transformers** 🤗: distilgpt2 LLM (lightweight but quirky).

---

## Setup Instructions 🚀
Ready to run this locally? Here’s the fun part!

1. **Clone or Create**:
   - Make a folder: `mkdir ai-customer-support-agent` 📂
   - `cd ai-customer-support-agent`

2. **Virtual Environment**:
   - `python -m venv venv` 🌀
   - Activate it: `source venv/bin/activate` (macOS/Linux) or `venv\Scripts\activate` (Windows) ✅

3. **Install Dependencies**:
   - `pip install flask langchain-community langchain-huggingface faiss-cpu transformers sentence-transformers` 📦
   - Boom, you’re loaded!

4. **Add FAQ File**:
   - Create `faq.txt` with this (blank lines between entries!):

Q: How do I track my order?
A: Visit our tracking page at example.com/track with your order ID.

Q: What is your return policy?
A: Returns are accepted within 30 days with a receipt.

Q: How do I contact support?
A: Email us at support@example.com or call 1-800-555-1234.

Q: Whom do I email for support?
A: Email us at support@example.com.

Q: Whom do I call for support?
A: Call 1-800-555-1234.



5. **Run the App**:
- `python app.py` 🔥
- Open `http://127.0.0.1:5000/` in your browser! 🌍

6. **Stop It**:
- Hit `Ctrl + C` in the terminal. Donezo! ✋

7. **Exit Venv**:
- `deactivate`—back to reality! 🌏

---

## Testing Scenarios 🧪🎉
Let’s see this AI in action! Here’s how to test it and what to expect. Type these into the query box and watch the magic! ✨

| **Query**                | **Expected Response**                                                                 | **Why It’s Cool**                     |
|--------------------------|---------------------------------------------------------------------------------------|---------------------------------------|
| "How do I track my order?" | "You can visit our tracking page at example.com/track with your order id."           | Nails the FAQ lookup! 📦            |
| "How do I contact support?" | "You can email us at support@example.com or call 1-800-555-1234."                   | Perfect contact info! 📞            |
| "Whom to mail for support?" | "You can email us at support@example.com."                                          | Short and sweet! ✉️                |
| "What’s your return policy?" | "You can returns are accepted within 30 days with a receipt."                      | Grammar’s a bit off, but it works! 🔄 |
| "Urgent help!"           | "I don’t have specific info for urgent requests. I’m sorry, I can’t assist further. Escalating to a human agent." | Escalation FTW! 🆘                 |
| "What day is today?"     | "I don’t have that information. I’m sorry, I can’t assist further. Escalating to a human agent." | Knows its limits! 🤷‍♂️            |

**Pro Tip**: Watch the terminal for debug logs—see what it retrieves and selects! 🕵️‍♂️

---

## What’s Next? 🚀
Week 2’s coming with:
- **Chat History** 💬: See all your convos!
- **Multi-Language** 🌍: Hola, Español support!
- More polish for that A+ grade! 🌟

---

## Troubleshooting 😱
- **Weird Answers?**: Check `faq.txt`—blank lines matter!
- **Errors?**: Did you `pip install` everything? Run in `(venv)`?
- **Stuck?**: Ctrl + C to stop, `deactivate` to exit, then holler at me!

---

## Key Capabilities 🎓
- **AI Power**: RAG + LangGraph = cutting-edge stuff! 🧠
- **System Design**: Local setup preps for distributed systems. 🌐
- **Fun Factor**: It’s a chatbot with customer obsession 😄

 🎉
