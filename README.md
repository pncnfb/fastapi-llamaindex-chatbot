# chatbot

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

3. (a) Install dependencies in editable mode

    ```bash
    uv pip install -e .
    ````

3. (b) Generate requirements.txt (for render deploy)

    ```bash
    uv pip compile pyproject.toml -o requirements.txt
    ```

4. Activate the virtual environment

    ```bash
    source .venv/bin/activate
    ```