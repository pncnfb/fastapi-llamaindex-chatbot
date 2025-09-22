# FastAPI Llamaindex Chatbot (ReAct Agent + Memory)

Clean implementation of a Chatbot using Llamaindex and FastAPI
## ⚙️ Setup

### 🐍 Virtual Environment

This project uses [uv](https://github.com/astral-sh/uv) for Python environment and dependency management.

1. Install `uv`

    ```bash
    brew install uv
    ```

2. Create a virtual environment with Python 3.12

    ```bash
    uv venv --python=3.12
    ```

3.  Install dependencies in editable mode

    ```bash
    uv pip install -e .
    ````

4. Activate the virtual environment

    ```bash
    source .venv/bin/activate
    ```
## ▶️ Run the App
To launch the FastAPI application with hot reloading in development mode:

```bash
uvicorn src.main:app --reload
```