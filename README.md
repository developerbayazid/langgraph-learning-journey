# LangGraph Learning Journey 🚀

My hands-on learning journey with **LangGraph**, exploring LLM applications, workflow orchestration, and AI agent development through practical projects and experiments.

This repository contains the code, examples, and notes I build while learning LangGraph step by step.

## 🎯 Goals

- Understand LangGraph fundamentals and core concepts.
- Build sequential, conditional, and parallel workflows.
- Learn how to manage state and control workflow execution.
- Explore nodes, edges, reducers, and graph-based architectures.
- Integrate Large Language Models (LLMs) into workflows.
- Understand workflow synchronization and conditional routing.
- Progress toward building practical AI agents and applications.

## 📚 Learning Projects

| Project                                   | Concepts                                                                   | Status       |
| ----------------------------------------- | -------------------------------------------------------------------------- | ------------ |
| Sequential Workflow                       | Nodes, Edges, State, Sequential Execution                                  | ✅ Completed |
| Parallel Workflow - Employee Analytics    | Parallel Execution, State Management, Fan-in Synchronization               | ✅ Completed |
| Parallel Workflow - Essay Evaluator       | Structured Output, Reducers, Parallel Execution, Average Score Calculation | ✅ Completed |
| Conditional Workflow - Content Moderation | Conditional Routing, Decision Making, Multiple Execution Paths             | ✅ Completed |
| LLM-Based Content Moderation              | LLM Integration, Content Analysis                                          | 📝 Planned   |
| Human-in-the-Loop Workflow                | Human Approval, Workflow Interruptions                                     | 📝 Planned   |

_More projects will be added as I progress through the learning series._

## 🛠️ Tech Stack

- **Language:** Python
- **Workflow Framework:** LangGraph
- **LLM Framework:** LangChain
- **LLM Provider:** OpenAI
- **Data Validation:** Pydantic
- **Environment Management:** Python Virtual Environment / uv
- **Environment Variables:** python-dotenv
- **Development Environment:** Jupyter Notebook / Python
- **Version Control:** Git & GitHub

## 📁 Repository Structure

```text
langgraph-learning-journey/
│
├── README.md
├── .gitignore
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
│   └── content_moderation.py
│
└── ...
```

_The repository structure will evolve as new projects and concepts are added._

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/langgraph-learning-journey.git

cd langgraph-learning-journey
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

Using Python:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Alternatively, use `uv` to manage the environment:

```bash
uv sync
```

### 3. Install dependencies

Install the required packages:

```bash
pip install langgraph langchain langchain-openai python-dotenv pydantic
```

### 4. Configure environment variables

Create a `.env` file in the project root or the relevant project directory.

```env
OPENAI_API_KEY=your_api_key_here
```

Never commit your actual API keys or secrets to GitHub.

### 5. Run a project

Navigate to the relevant project directory.

For example:

```bash
cd parallel-workflow

python employee_analytics_workflow.py
```

Or run using `uv`:

```bash
uv run parallel-workflow/employee_analytics_workflow.py
```

Adjust the entry-point filename according to the project you want to execute.

## 🧠 Key Concepts

Topics explored and planned throughout this learning journey:

- Graph-based Workflow Architecture
- State Management with TypedDict
- Nodes and Edges
- Sequential Execution
- Conditional Routing
- Parallel Execution
- Fan-in Synchronization
- Reducers and State Updates
- Structured Output with Pydantic
- LLM Integration
- Tool Calling
- Memory and Persistence
- Checkpointing
- Human-in-the-Loop Workflows
- AI Agent Development

## 📈 Progress Tracking

I will continuously update this repository as I complete new lessons, implement workflows, and experiment with new concepts.

Each project may include:

- Source code and implementation examples
- Project-specific README files
- Workflow architecture diagrams
- Example inputs and outputs
- Notes explaining important concepts

## 📖 Learning Resources

- [LangGraph Documentation](https://docs.langchain.com/oss/python/langgraph/overview)
- [LangChain Documentation](https://docs.langchain.com/oss/python/langchain/overview)

## 🤝 Contributions

This repository is primarily a personal learning project. Suggestions, feedback, and discussions are welcome.

## 📄 License

This project is currently intended for educational and learning purposes. A license may be added in the future.

---

**Learning by building, one workflow at a time.** 🚀
