# 🚀 SkillMap AI Agent

An AI-powered Skill-to-Career Mapping Agent that helps users analyze industry skill demand, explore career opportunities, and discover real-time job openings using autonomous AI agent workflows.

Built with LangChain, Google Gemini, Tavily Search, JSearch API, and Streamlit.

---

## 📌 Overview

Choosing the right career path often requires researching multiple sources for market demand, job trends, and available opportunities.

SkillMap AI Agent simplifies this process by combining real-time web search, job discovery, and AI-powered reasoning into a single application.

Users can simply enter a skill such as:

```text
Generative AI
Python
Data Science
Machine Learning
React
```

and receive:

- Industry demand insights
- Career opportunities
- Market trends
- Live job openings
- Direct application links

---

## ✨ Features

### 📈 Skill Demand Analysis
- Analyzes current industry demand for a skill
- Identifies growth trends and adoption patterns
- Provides market insights using real-time search

### 💼 Career Opportunity Discovery
- Suggests roles related to selected skills
- Explains career paths and job responsibilities
- Highlights in-demand positions

### 🔥 Real-Time Job Search
- Retrieves live job openings
- Displays company information
- Provides application URLs
- Supports location-based searches

### 🤖 Autonomous AI Agent
- Uses LangChain's Agent Architecture
- Performs tool selection automatically
- Combines multiple tool outputs into a single response

### 🎨 Interactive User Interface
- Built with Streamlit
- Simple and responsive design
- Real-time results

---

## 🏗️ Architecture

```text
User Query
    │
    ▼
Streamlit UI
    │
    ▼
LangChain Agent
    │
    ▼
Google Gemini
    │
 ┌──┴───────────────┐
 ▼                  ▼
Tavily Search    JSearch API
(Skill Demand)   (Job Search)
 └──────┬──────────┘
        ▼
 AI Reasoning Layer
        ▼
 Final Response
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Core Development |
| LangChain | Agent Framework |
| Google Gemini | LLM & Reasoning Engine |
| Tavily Search | Real-Time Web Search |
| JSearch API | Live Job Search |
| Streamlit | User Interface |
| REST APIs | External Integrations |

---

## 📂 Project Structure

```text
skillmap-ai-agent/
│
├── app.py
├── agents.py
├── tools.py
├── prompts.py
├── requirements.txt
├── README.md
│
└── .streamlit/
    └── secrets.toml
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/skillmap-ai-agent.git

cd skillmap-ai-agent
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Required API Keys

Create a `.streamlit/secrets.toml` file:

```toml
GOOGLE_API_KEY = "your_google_api_key"
TAVILY_API_KEY = "your_tavily_api_key"
RAPID_API_KEY = "your_rapidapi_key"
```

Required Services:

- Google Gemini API
- Tavily Search API
- RapidAPI (JSearch)

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Application URL:

```text
http://localhost:8501
```

---

## 💡 Example Queries

```text
What is the demand for Generative AI in India?
```

```text
Show Python developer jobs in Hyderabad
```

```text
Find Machine Learning opportunities for freshers
```

```text
What career paths are available for Data Science?
```

---

## 🚀 Future Enhancements

- Resume Upload & ATS Matching
- Personalized Job Recommendations
- Salary Insights Tool
- Career Roadmap Generator
- Interview Preparation Assistant
- LangGraph Multi-Agent Workflow
- Skill Gap Analysis
- Learning Resource Recommendations

---

## 🎯 Learning Outcomes

Through this project:

- Built AI Agents using LangChain
- Implemented Tool Calling Architecture
- Integrated Multiple APIs
- Worked with Real-Time Data Sources
- Developed Agentic AI Applications
- Built End-to-End Streamlit Deployment

---

## 👨‍💻 Author

**Harsha**

Engineering Student | AI & GenAI Enthusiast | Python Developer

---

⭐ If you found this project useful, consider giving it a star.
