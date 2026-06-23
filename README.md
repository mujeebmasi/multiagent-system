# 🤖 Multi-Agent Research System

A powerful AI-driven research assistant that leverages multiple specialized agents to gather, analyze, and synthesize information from the web. Built using Gemini, Mistral AI, Tavily Search, and Streamlit, the system automates the research process by coordinating multiple agents working together toward a common objective.

---

## 📌 Overview

The Multi-Agent Research System is designed to perform deep research on user-provided topics by combining the strengths of multiple AI models and web search capabilities.

Instead of relying on a single LLM response, the system breaks research into specialized tasks handled by dedicated agents, resulting in more comprehensive and accurate outputs.

---

## ✨ Features

* 🔍 Real-Time Web Research using Tavily
* 🤖 Multi-Agent Architecture
* 🧠 Gemini Integration
* ⚡ Mistral AI Integration
* 📄 Automated Research Report Generation
* 🌐 Web Information Retrieval
* 📊 Structured Research Summaries
* 🎨 Streamlit User Interface
* 🚀 Fast and Scalable Workflow

---

## 🏗️ Architecture

The system follows a collaborative multi-agent workflow:

### Research Agent

* Searches for relevant information
* Collects web sources
* Extracts key insights

### Analysis Agent

* Evaluates gathered information
* Identifies important findings
* Removes irrelevant content

### Report Generation Agent

* Synthesizes research results
* Generates structured reports
* Produces concise summaries

---

## 🔄 Workflow

```text
User Query
     │
     ▼
Research Agent
     │
     ▼
Tavily Search API
     │
     ▼
Analysis Agent
     │
     ▼
Gemini / Mistral
     │
     ▼
Report Generation Agent
     │
     ▼
Final Research Report
```

---

## 🛠 Tech Stack

### AI Models

* Google Gemini
* Mistral AI

### Search & Retrieval

* Tavily Search API

### Backend

* Python

### Frontend

* Streamlit

### Libraries

* Requests
* Python-dotenv
* Streamlit
* Google Generative AI SDK

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/mujeebmasi/multiagent-system.git

cd multiagent-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_key

MISTRAL_API_KEY=your_mistral_key

TAVILY_API_KEY=your_tavily_key
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 📊 Example Use Cases

* Academic Research
* Market Research
* Technology Trend Analysis
* Competitor Analysis
* Literature Reviews
* Business Intelligence
* Industry Reports

---

## 🎯 Key Benefits

* Faster information gathering
* More comprehensive research outputs
* Reduced manual effort
* Multi-model validation of results
* Improved research quality through agent collaboration

---

## 🔮 Future Improvements

* PDF Report Export
* Citation Generation
* Research Memory
* Multi-Source Verification
* Agent Performance Monitoring
* Research History Dashboard

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Abdul Mujeeb**

AI Developer | Multi-Agent Systems | LLM Applications

Built using Gemini, Mistral AI, Tavily Search, Python, and Streamlit.
