# LangGraph Learning Journey

A hands-on learning journey to understand and build AI workflows and agents using **LangChain** and **LangGraph**.

This repository contains practical implementations of different workflow architectures, from basic sequential execution to parallel processing and conditional routing.

## 🎯 Learning Goals

- Understand LangGraph fundamentals and graph-based architecture.
- Learn how nodes, edges, state, and reducers work.
- Build sequential, parallel, and conditional workflows.
- Work with LLMs using LangChain.
- Implement structured outputs using Pydantic.
- Understand state management and workflow execution.
- Gradually explore advanced LangGraph concepts and AI agents.

## 🛠️ Tech Stack

- **Python** — Primary programming language
- **LangGraph** — Workflow orchestration
- **LangChain** — LLM application framework
- **OpenAI** — Language models
- **Pydantic** — Structured output and data validation
- **python-dotenv** — Environment variable management
- **JupyterLab** — Experimentation and learning
- **Git & GitHub** — Version control

## 📂 Repository Structure

```text
langgraph-learning-journey/
│
├── README.md
├── .gitignore
│
└── workflows/
    │
    ├── sequential-workflow/
    │   ├── README.md
    │   └── main.py
    │
    ├── parallel-workflow/
    │   ├── README.md
    │   ├── employee_analytics_workflow.py
    │   └── essay_evaluator.py
    │
    ├── conditional-workflow/
    │   ├── README.md
    │   ├── content_moderation_workflow.py
    │   └── customer_review_analysis.py
    │
    └── ...
```

## 📚 Learning Progress

### 1. Sequential Workflow

\<details>
\<summary>\<strong>Employee Analytics Workflow — Completed\</strong>\</summary>

**Concepts learned:**

- Sequential node execution
- State management
- Node dependencies
- Graph edges
- Fan-in synchronization

**Workflow:**

```text
START
  |
  ├── Calculate Yearly Salary
  |           |
  |      Calculate Bonus
  |
  └── Project Evaluation
              |
              |
       Summary Generation
              |
             END
```

\</details>

### 2. Parallel Workflow

\<details>
\<summary>\<strong>Employee Analytics Workflow — Completed\</strong>\</summary>

**Concepts learned:**

- Parallel node execution
- Multiple branches
- Fan-in synchronization
- Combining parallel results

\</details>

\<details>
\<summary>\<strong>Essay Evaluator — Completed\</strong>\</summary>

An AI-powered essay evaluation system that evaluates essays through multiple parallel evaluation nodes.

**Evaluation dimensions:**

- Language quality
- Content analysis
- Clarity and coherence

**Concepts learned:**

- Parallel execution
- Pydantic structured output
- `Annotated` and reducers
- `operator.add`
- Aggregating results from parallel nodes
- Average score calculation

\</details>

### 3. Conditional Workflow

\<details>
\<summary>\<strong>Content Moderation Workflow — Completed\</strong>\</summary>

A content moderation system that checks submitted posts and routes them according to moderation results.

**Possible outcomes:**

- Approved
- Flagged for review
- Rejected

**Concepts learned:**

- Conditional edges
- Dynamic routing
- Routing functions
- `Literal` type hints
- Branching execution

\</details>

\<details>
\<summary>\<strong>Customer Review Analysis — Completed\</strong>\</summary>

An AI-powered customer review analysis system that detects sentiment and generates an appropriate response.

**Workflow behavior:**

- First, identify whether the customer review is positive or negative.
- For positive reviews, generate a warm thank-you response.
- For negative reviews, diagnose the issue and generate an empathetic support response.

**Diagnosis categories:**

- Issue type: UI, UX, Performance, Bug, Support, or Other
- Tone: Angry, Frustrated, Disappointed, or Calm
- Urgency: Low, Medium, or High

**Concepts learned:**

- Conditional routing
- Structured output with Pydantic
- Multiple structured-output schemas
- Sentiment analysis
- Issue diagnosis
- LLM-powered response generation
- Branch-specific node execution

**Workflow:**

```text
              START
                |
         Find Sentiment
                |
          Conditional
           Routing
           /      \
      Positive   Negative
         |          |
   Generate      Run Diagnosis
   Response          |
         |      Negative Response
         |          |
         END        END
```

\</details>

## 🚧 Upcoming Topics

- [x] LLM-Based Content Moderation
- [ ] Human-in-the-Loop Workflow
- [ ] Tool Calling and Tool Integration
- [ ] State Management and Reducers
- [ ] Checkpointing and Persistence
- [ ] Memory Management
- [ ] Multi-Agent Systems
- [ ] LangGraph Deployment

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/langgraph-learning-journey.git

cd langgraph-learning-journey
```

### 2. Create a virtual environment

Using Python:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install langgraph langchain langchain-openai pydantic python-dotenv
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
```

**Important:** Never commit your `.env` file or expose your API key.

## ▶️ Running Workflows

Run individual workflows from the repository root.

### Sequential Workflow

```bash
python workflows/sequential-workflow/main.py
```

### Parallel Workflow

```bash
python workflows/parallel-workflow/employee_analytics_workflow.py
```

```bash
python workflows/parallel-workflow/essay_evaluator.py
```

### Conditional Workflow

```bash
python workflows/conditional-workflow/content_moderation_workflow.py
```

```bash
python workflows/conditional-workflow/customer_review_analysis.py
```

## 📖 Learning Resources

- [LangGraph Documentation](https://docs.langchain.com/oss/python/langgraph/overview)
- [LangChain Documentation](https://docs.langchain.com/oss/python/langchain/overview)
- [LangGraph Learning Playlist](https://www.youtube.com/playlist?list=PLkz_y24mlSJZ9SFlc9O4Q4Grli5SQDbrB)

## 💡 My Learning Approach

I am following a practical, project-based learning approach:

1. Understand a concept.
2. Implement it with Python and LangGraph.
3. Test the workflow with different inputs.
4. Understand how state flows between nodes.
5. Document the implementation.
6. Move on to more advanced concepts.

The goal is not just to learn the syntax, but to understand how real-world AI workflows and agents are designed and implemented.

---

**This repository is continuously evolving as I learn and explore LangGraph.**
