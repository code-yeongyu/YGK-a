# Python Poetry Template

This template is designed to make it easy to set up a Python project that is well-structured, organized, and easy to maintain. It comes pre-configured with several tools that will help you develop your project more efficiently, including:

- Visual Studio Code integration: with the `RunOnSave`, `even-better-toml` and `ruff` extensions installed, you can format, lint, and type-check your code automatically every time you save a file.
- Type checking: this template is configured to use `mypy` and `pyright` to automatically infer types when possible, without imposing strict typing requirements on your code.
- Linting: `ruff`, an extremely fast Python linter, written in Rust is configured well to help you catch and fix code style issues.
- Formatting: `yapf`, `ruff`, and `unify` are configured to help you keep your code clean and well-organized.
- Testing: `pytest` is configured to make it easy to run tests, and `pytest-cov` is configured to help you measure code coverage.
- Dependency management: `poetry` is configured to help you manage your project's dependencies.
- Toolkits: `invoke` is configured to provide a range of useful tasks, such as running your code, running tests, formatting your code, and checking your code style and types. These tasks are fully configurable in the [tasks.py](tasks.py) file.

## Installation

To install this template, simply follow these steps:

```sh
git clone git@github.com:code-yeongyu/Python-Poetry-Template.git
cd Python-Poetry-Template
poetry install
code --install-extension emeraldwalk.RunOnSave
code --install-extension tamasfe.even-better-toml
code --install-extension charliermarsh.ruff
```

## Usage

To use this template, you can follow these steps:

### Open Shell

To open a shell in the project directory, use the following command:

```sh
poetry shell
```

### Name your project

```sh
invoke rename-project <your-project-name>
```

### Run Code

To run your code, use the following command:

```sh
poetry run invoke run
```

### Run Tests

To run your tests, use the following command:

```sh
poetry run invoke test
```

### Run Formatters

To run the code formatters, use the following command:

```sh
poetry run invoke format_code
```

### Run Checking Code Style & Type hint

To check your code style and type hints, use the following command:

```sh
poetry run invoke check
```
