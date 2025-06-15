# 🧠 AI Research Assistant

A smart research assistant powered by LangChain and OpenAI/Anthropic models. It can fetch, summarize, and structure information using custom tools and generate a detailed research report.

---

## 📌 Description

This project is a CLI-based AI Research Assistant designed to automate the research process using modern LLMs. By integrating tools like web search, Wikipedia lookup, and a custom save feature, it allows users to generate topic-based structured research outputs using `langchain` agents and prompt engineering.

---

## ✨ Features

- 🔍 **Multi-source research** using tools like Web Search and Wikipedia  
- 🧾 **Structured response output** using `Pydantic` models  
- 🧠 **LLM support** for GPT-4o-mini (OpenAI) and Anthropic Claude (configurable)  
- 🛠️ **Tool-based agent orchestration** using LangChain's `AgentExecutor`  
- 💾 **Custom Save Tool** to optionally persist the results  
- 🧪 **Prompt template engineering** for dynamic formatting  

---

## 🛠️ Tech Stack

- Python  
- LangChain  
- OpenAI GPT-4o-mini  
- Pydantic  
- dotenv  
- Custom Tool Integration (search, wiki, save)  

---

## 🚀 How to Run

### 1. **Clone the Repository**
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

> Make sure `langchain`, `pydantic`, `python-dotenv`, `openai`, and any tools used are included in `requirements.txt`.

### 3. **Set Environment Variables**

Create a `.env` file in the root directory and add your API keys:

```env
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
```

### 4. **Run the Assistant**

```bash
python main.py
```

You'll be prompted to enter a research query. The assistant will process the query, invoke relevant tools, and return a structured output.

---

## 📂 Output Format

The response is structured as follows:

```json
{
  "topic": "The topic you asked about",
  "summary": "Concise, AI-generated research summary",
  "sources": ["List", "of", "sources", "used"],
  "tools_used": ["search_tool", "wiki_tool"]
}
```

---

## 🔧 Tools Used

The assistant is equipped with:

- `search_tool` – for web search  
- `wiki_tool` – for Wikipedia summaries  
- `save_tool` – to persist the research (implementation-specific)  

> These are defined in a separate `tools.py` module.

---

## 📎 Example Query

```
Enter your research query: Future of quantum computing
```

> Output will include a structured research summary using multiple sources.

---

## ✅ Future Improvements

- Web UI with Streamlit or FastAPI  
- Optional export to PDF/Markdown  
- Tool selection based on query type  
- Real-time source linking  

---

## 🤝 Contributing

Feel free to open issues, suggest improvements, or submit PRs!

---

## 🪪 License

MIT License

---

## 🙌 Acknowledgements

- [LangChain](https://www.langchain.com/)  
- [OpenAI](https://platform.openai.com/)  
- [Anthropic](https://www.anthropic.com/)
