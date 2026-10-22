<!-- Header -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=200&section=header&text=Ph%E1%BA%A1m%20%C4%90%C3%ACnh%20Duy&fontSize=48&fontColor=ffffff&fontAlignY=36&desc=Data%20Scientist%20%C2%B7%20AI%20Engineer&descAlignY=58&descSize=18" alt="Phạm Đình Duy — Data Scientist · AI Engineer" width="100%"/>
</p>

<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=20&duration=3200&pause=900&color=38BDF8&center=true&vCenter=true&width=720&lines=Knowledge-graph+RAG+with+citations+you+can+check;Stateful+LLM+agents+built+on+LangGraph;Retrieval+evaluation+%C2%B7+LLM-as-Judge+%C2%B7+golden+sets;From+notebook+to+FastAPI%2C+Docker+and+CI%2FCD" alt="Typing intro"/>
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/📍_Hanoi,_Vietnam-1e293b?style=flat-square" alt="Hanoi, Vietnam"/>
  <img src="https://img.shields.io/badge/🎓_B.Sc._Data_Science_@_USTH-1e293b?style=flat-square" alt="USTH"/>
  <img src="https://img.shields.io/badge/🔬_Research_Intern_@_IOIT_(VAST)-1e293b?style=flat-square" alt="IOIT VAST"/>
  <img src="https://img.shields.io/badge/✅_Open_to_AI_/_Data_roles-16a34a?style=flat-square" alt="Open to work"/>
</p>

<p align="center">
  <a href="mailto:kayne6842@gmail.com"><img src="https://img.shields.io/badge/Email-kayne6842@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
  <a href="https://github.com/Dzzuy"><img src="https://img.shields.io/badge/GitHub-Dzzuy-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Dzzuy"/></a>
  <a href="https://github.com/Dzuy123"><img src="https://img.shields.io/badge/GitHub-Dzuy123-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Dzuy123"/></a>
</p>

---

## 👋 About me

I'm a **Data Science student at the University of Science and Technology of Hanoi (USTH)** who builds applied AI systems that have to hold up outside a notebook. My work sits where **retrieval, agents and evaluation** meet: I like systems that cite their sources, say "I don't know" when the evidence is missing, and come with numbers that show how well they work.

- 🔭 **Now:** Research Intern at the **Institute of Information Technology, Vietnam Academy of Science and Technology**, building a knowledge-graph RAG system for Vietnamese labour law and HR policy.
- 🏗️ **Training:** VinUni **AI Practical Competency Program**, AI & Data Infrastructure track: data pipelines, feature stores, model serving, CI/CD, cloud, LLMOps and observability.
- 🧭 **Leadership:** led 3 team projects (a VinFast sales-coaching platform and two USTH research projects) plus a 4-person team in a 39-hour AI hackathon.

---

## 🎓 Education & awards

<table>
<tr>
<td width="50%" valign="top">

### University of Science and Technology of Hanoi (USTH)
**Bachelor's in Data Science** · 2022 – present · Hanoi, Vietnam

| Year | GPA |
|---|---|
| 1st year | **3.08 / 4.0** |
| 2nd year | **3.23 / 4.0** |
| 3rd year | **3.22 / 4.0** |

</td>
<td width="50%" valign="top">

### 🏅 Awards & certifications
- **USTH AS Merit Scholarship**<br/><sub>University of Science and Technology of Hanoi · 2023</sub>
- **VinUni AI Practical Competency Program**<br/><sub>AI & Data Infrastructure track · 2026</sub>

</td>
</tr>
</table>

## 🌏 Languages

<p>
  <img src="https://img.shields.io/badge/🇻🇳_Vietnamese-Native-16a34a?style=for-the-badge" alt="Vietnamese: Native"/>
  <img src="https://img.shields.io/badge/🇬🇧_English-Fluent-2563eb?style=for-the-badge" alt="English: Fluent"/>
  <img src="https://img.shields.io/badge/🇹🇭_Thai-Intermediate-9333ea?style=for-the-badge" alt="Thai: Intermediate"/>
  <img src="https://img.shields.io/badge/🇫🇷_French-A2-ea580c?style=for-the-badge" alt="French: A2"/>
</p>

---

## 📊 Results in numbers

<table align="center">
  <tr>
    <td align="center" width="25%"><h2>96.5%</h2><sub>context hit rate<br/><b>KG-RAG, labour law</b></sub></td>
    <td align="center" width="25%"><h2>88.5%</h2><sub>compliance accuracy<br/><b>93-question policy set</b></sub></td>
    <td align="center" width="25%"><h2>96.4%</h2><sub>macro-F1<br/><b>Parkinson's motion classifier</b></sub></td>
    <td align="center" width="25%"><h2>122 yrs</h2><sub>of climate records<br/><b>SE Asia drought study</b></sub></td>
  </tr>
</table>

---

## 🚀 Featured projects

### ⚖️ [Knowledge-Graph RAG for Vietnamese Labour Law & HR Policies](https://github.com/Dzuy123/KG-RAG-Labour-Law-Company-Policies)
<sub>Bachelor thesis · IOIT (VAST) internship · 2026</sub>

A chatbot that answers HR and legal questions from **two sources at once**, Vietnamese labour law and a company's HR handbook, and checks whether each policy complies with the law. Every answer comes with law evidence, policy evidence, citations, a compliance note and a confidence level.

- Parsed the legal corpus and HR handbook into article-level records, then linked policy sections to law articles in **Neo4j** with labelled `IMPLEMENTS` edges (`COMPLIANT`, `MORE_FAVORABLE`, …)
- Hybrid retrieval: **BGE-M3** vectors in ChromaDB + **BM25** for article numbers and legal phrases, fused with **reciprocal rank fusion** and reranked by a cross-encoder; compared 5 retrieval configurations
- **96.5% context hit rate** and **74.4% compliance accuracy** on 114 questions; **88.5%** compliance accuracy on a separate 93-question set, measured with RAGAS plus custom citation and compliance metrics
- Shipped as a **Django** web app with login, chat history and a source / knowledge-graph viewer

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white) ![Neo4j](https://img.shields.io/badge/Neo4j-4581C3?style=flat-square&logo=neo4j&logoColor=white) ![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6F61?style=flat-square) ![BGE-M3](https://img.shields.io/badge/BGE--M3-FFD21E?style=flat-square&logo=huggingface&logoColor=black) ![RAGAS](https://img.shields.io/badge/RAGAS-6D28D9?style=flat-square)

---

### 🚗 [AI Sales Coach for VinFast Advisors](https://github.com/Dzzuy/P-043-Hosting)
<sub>Team leader · VinAI internship project · 2026 · <a href="https://aisale.itup.io.vn/">live demo</a></sub>

New car-sales advisors need hours of one-on-one coaching and can easily quote the wrong spec or price. This platform lets them **practise with an AI customer** before meeting real ones, and gives managers evidence-backed scorecards to review instead of sitting in on every session.

- **Practice Room:** multi-turn roleplay (text or voice) with AI customers who have personas and hidden facts, covering needs discovery, objections, product explanations and closing
- Multi-turn **LangGraph** state with checkpoints and **recovery for interrupted sessions**
- A separate **LLM judge** scores each session against a rubric, cites transcript evidence and fact-checks product and policy claims; managers approve or edit the score
- **Copilot:** source-cited Q&A over vehicle specs and policies that refuses to answer when evidence is missing
- Full stack: FastAPI + React 19, PostgreSQL + pgvector, Docker Compose, GitHub Actions, deployed on Render and Vercel

![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langchain&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![React](https://img.shields.io/badge/React_19-20232A?style=flat-square&logo=react&logoColor=61DAFB) ![PostgreSQL](https://img.shields.io/badge/pgvector-4169E1?style=flat-square&logo=postgresql&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/CI-2088FF?style=flat-square&logo=githubactions&logoColor=white)

---

<table>
<tr>
<td width="50%" valign="top">

### 🎬 [MetaBERT4Rec](https://github.com/Dzuy123/movie-transformer-recommender)
<sub>Genre-aware film recommendation · team project</sub>

Extended **BERT4Rec** with learnable genre embeddings, so the model learns from item, position and genre together. Trained 3 configurations for 50 epochs on **MovieLens 20M** and evaluated Recall@K, NDCG@K and MRR under 3 negative-sampling strategies.

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white) ![Transformers](https://img.shields.io/badge/Transformers-FFD21E?style=flat-square&logo=huggingface&logoColor=black)

</td>
<td width="50%" valign="top">

### 🖐️ [Parkinson's Hand-Movement Classification](https://github.com/Dzuy123/ParkinsonsTremorClassification)
<sub>Machine learning in medicine · team leader</sub>

Engineered temporal, geometric, statistical and frequency features from hand-landmark data to classify 5 Parkinson's motor-assessment exercises. **96.88% accuracy / 96.37% macro-F1** with CatBoost under 5-fold CV, with subject-level generalization limits documented honestly.

![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white) ![CatBoost](https://img.shields.io/badge/CatBoost-FFCC00?style=flat-square&logoColor=black)

</td>
</tr>
<tr>
<td colspan="2" valign="top">

### 🌾 [Spatiotemporal Drought Risk · SPEI](https://github.com/Dzuy123/SPEI_analysis)
<sub>Climate statistics · team leader</sub>

Analysed **122 years** (1901–2022) of SPEI-6 records across Southeast Asia: raster processing, drought-event detection, distribution fitting by MLE with AIC/BIC, and **bivariate copulas** for joint duration–severity return periods.

![R](https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white) ![LaTeX](https://img.shields.io/badge/LaTeX-008080?style=flat-square&logo=latex&logoColor=white)

</td>
</tr>
</table>

---

## 🛠️ Tech stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,r,pytorch,sklearn,postgres,redis,fastapi,django,react,ts,docker,githubactions,aws,linux,git&perline=8" alt="Tech stack icons"/>
</p>

| Area | Tools |
|---|---|
| **ML & Data Science** | Python, R, SQL, PyTorch, scikit-learn, CatBoost, XGBoost, pandas, NumPy, Hugging Face Transformers, feature engineering, statistical modelling |
| **GenAI & Agents** | LangGraph, LangChain, RAG, tool calling, structured outputs, prompt engineering, multi-agent / MCP |
| **Retrieval** | Neo4j, ChromaDB, Qdrant, pgvector, BGE-M3, BM25, hybrid search, RRF, cross-encoder reranking |
| **Evaluation** | RAGAS, LLM-as-Judge, golden datasets, rubric scoring, cross-validation, Recall/NDCG/MRR |
| **Backend** | FastAPI, Django, REST APIs, PostgreSQL, Redis, Pydantic, pytest |
| **Data & MLOps** | DuckDB, dbt, Parquet, Feast, DVC, MLflow, Docker, GitHub Actions, AWS, Terraform |
| **LLMOps & Reliability** | LangSmith, Langfuse, structured logging, tracing, SLOs, guardrails, red-teaming |

---

<details>
<summary><b>🧪 VinUni AI Practical Competency Program: 25+ hands-on labs (click to expand)</b></summary>
<br/>

Daily production-style labs completed in 2026, all public on [@Dzzuy](https://github.com/Dzzuy?tab=repositories):

| Theme | Labs |
|---|---|
| **LLM foundations** | LLM foundations · prompt engineering & tool calling · AI product labs |
| **RAG & agents** | RAG pipeline · multi-agent systems with MCP & A2A · agent arena gateway |
| **Data engineering** | Data pipeline engineering · data observability · lakehouse · vector & feature store |
| **Infrastructure** | Cloud AI infrastructure (Terraform) · cloud deployment · model serving · GPU FinOps |
| **MLOps & LLMOps** | CI/CD for AI systems · prompt versioning · monitoring, tracing & SLOs · AI evaluation |
| **Responsible AI** | Guardrails, human-in-the-loop, red team / blue team · data governance, agent containment & supply-chain security |

Also led a 4-person team in a **39-hour AI product hackathon** (SPEC → prototype → demo) as team lead and AI engineer.

</details>

---

## 📈 GitHub activity

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=Dzzuy&show_icons=true&hide_border=true&theme=tokyonight&include_all_commits=true&count_private=true" alt="GitHub stats"/>
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Dzzuy&layout=compact&hide_border=true&theme=tokyonight&langs_count=8" alt="Top languages"/>
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=Dzzuy&theme=tokyo-night&hide_border=true&area=true" alt="Contribution graph" width="95%"/>
</p>

---

## 🤝 Let's connect

I'm looking for **AI Engineer, Data Scientist and ML Engineer** roles and internships, especially on teams building **RAG, agents or evaluation** for real users. If that sounds like your team, I'd love to talk.

<p align="center">
  <a href="mailto:kayne6842@gmail.com"><img src="https://img.shields.io/badge/Say_hello-kayne6842@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email me"/></a>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,50:203a43,100:0f2027&height=110&section=footer" alt="" width="100%"/>
</p>
