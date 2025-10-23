
# 🤖 RAG Learning Roadmap

Master **Retrieval-Augmented Generation (RAG)** with this hands-on guide — from theory to production-ready systems!

## 📝 Overview

This repository is your roadmap to mastering **Retrieval-Augmented Generation (RAG)**, blending clear notes, practical projects, and an interactive UI. It assumes basic knowledge of LLMs and guides you through building, deploying, and optimizing RAG systems.

**What is RAG?**
RAG enhances LLMs by retrieving relevant external data, making responses **contextual**, **factual**, and **dynamic** — perfect for accurate, real-world AI applications.

## 🗂️ Table of Contents

| Chapter | Title                                                                                     | Notes                                                    |
| ------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| 1       | [Introduction to LLMs and RAG](docs/chapter_1.md)                                            | [Projects](projects/chapter_1/)                             |
| 2       | [Challenges in Building RAG Systems](docs/chapter_2.md)                                      | [Projects](projects/chapter_2/)                             |
| 3       | [Reduce Hallucinations with Prompting](docs/chapter_3.md)                                    | [Projects](projects/chapter_3/)                             |
| 4.1     | [Advanced Chunking Techniques](docs/chapter_4.md#advanced-chunking-techniques)               | [Projects](projects/chapter_4/chunking_embedding_pipeline/) |
| 4.2     | [Selecting Embedding Models](docs/chapter_4.md#how-to-select-an-embedding-model)             | [Projects](projects/chapter_4/reranking_vector_db/)         |
| 4.3     | [Choosing Vector Databases](docs/chapter_4.md#choosing-the-perfect-vector-database)          | [Projects](projects/chapter_4/reranking_vector_db/)         |
| 4.4     | [Selecting Reranking Models](docs/chapter_4.md#how-to-select-a-reranking-model)              | [Projects](projects/chapter_4/reranking_vector_db/)         |
| 4.5     | [Building Enterprise RAG Systems](docs/chapter_4.md#steps-to-build-an-enterprise-rag-system) | [Projects](projects/chapter_4/enterprise_rag_blueprint/)    |
| 5       | [8 Scenarios for Production Testing](docs/chapter_5.md)                                      | [Projects](projects/chapter_5/)                             |
| 6       | [Monitoring &amp; Optimizing RAG](docs/chapter_6.md)                                         | [Projects](projects/chapter_6/)                             |
| 7       | [Improving RAG with Metrics](docs/chapter_7.md)                                              | [Projects](projects/chapter_7/)                             |

## 🚀 How to Use This Repository

1. Read chapter notes in [`docs/`](docs/) for theory.
2. Run hands-on projects in [`projects/`](projects/) to apply concepts.
3. Launch the interactive UI in [`ui/`](ui/) to test all projects live.
4. Follow chapters in order for a structured learning path.

https://github.com/shishira-18/RAG-Learning-Roadmap.git

**Setup**:

```
git clone https://github.com/your-username/RAG-Learning-Roadmap.git
```

```
cd ui
```

```
pip install -r requirements.txt
```

```
streamlit run app.py

```

## 🧩 Repository Structure

```
RAG-Learning-Roadmap/  
├── README.md # Overview and roadmap  
├── docs/ # Learning notes (theory and explanations)  
│ ├── chapter_1.md  
│ ├── chapter_2.md  
│ ├── ...  
├── projects/ # Practical RAG projects  
│ ├── chapter_1/  
│ ├── chapter_2/  
│ ├── ...
```

## 🌟 What You'll Learn

- Core concepts of RAG and LLMs
- Chunking and embedding optimization
- Choosing the right vector and reranking models
- Building enterprise-grade RAG pipelines
- Monitoring and improving system performance

## 📚 Credits / References

- [Mastering RAG](https://galileo.ai/mastering-rag)

## 🤝 Contributing

We welcome your insights and improvements! Share tips, add examples, or suggest enhancements to make this RAG learning roadmap even better.

## ⭐ Support & Feedback

If this roadmap helps you, please **star this repo** 🌟 — it motivates continued work!
Have ideas, feedback, or RAG experiments to share? Open an issue or PR!
