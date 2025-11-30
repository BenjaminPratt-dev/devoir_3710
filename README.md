# INF3710 Assignment - Python Template

This is a complete Python project template for INF3710 assignments using `uv` for dependency management.

## Project Structure

```
python-project/
├── src/
│   ├── __init__.py
│   ├── main.py          # Main entry point
│   └── solution.py      # Your solution code
├── tests/
│   ├── __init__.py
│   └── test_solution.py # Your tests
├── pyproject.toml       # Project configuration
├── README.md
└── .vscode/             # VS Code settings
    ├── settings.json
    ├── extensions.json
    └── launch.json
```

## Getting Started

### 1. Install uv (if not already installed)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Initialize the project

```bash
cd python-project
uv sync
```

This will create a virtual environment and install all dependencies.

### 3. Run your solution

```bash
# Run the main script
uv run python src/main.py

# Or run directly
uv run src/main.py
```

### 4. Run tests

```bash
# Run all tests
uv run python tests/test_solution.py

# Or run directly if in virtual environment
python tests/test_solution.py
```


## Development Workflow

1. **Write your solution** in `src/solution.py`
2. **Write tests** in `tests/test_solution.py`
3. **Run tests locally** with `uv run python tests/test_solution.py`
4. **Test with stdin/stdout** using `src/main.py`
5. **Upload to Gradescope** (zip the entire directory)

## VS Code Integration

Open this folder in VS Code. The `.vscode/` settings will:
- Automatically select the uv virtual environment
- Enable Python linting and formatting
- Provide debugging support
- Show recommended extensions

### Recommended Extensions
- Python (ms-python.python)
- Pylance (ms-python.vscode-pylance)
- Ruff (charliermarsh.ruff)

## Gradescope Submission

You can submit either:
1. **Zip the entire project**: `zip -r solution.zip . -x ".*" -x "__pycache__/*" -x ".venv/*"`
2. **Individual files**: `pyproject.toml`, `src/*.py`

The autograder will:
1. Detect `pyproject.toml`
2. Run `uv sync` to install dependencies
3. Execute your code with `uv run`

## Tips

- Keep `dependencies = []` in `pyproject.toml` since external libraries aren't allowed
- Write tests using simple `assert` statements to validate your solution locally
- Run tests frequently during development
- Use type hints for better code quality
