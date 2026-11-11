# Git Practice Calculator

A small Python calculator project built for practicing Git and GitHub collaboration with a friend. It includes reusable calculation functions, a command-line program, and a Streamlit web interface.

## Features

- Addition, subtraction, multiplication, and division
- Squares, powers, square roots, and cube roots
- Division-by-zero and invalid square-root input handling
- Interactive command-line calculator
- Streamlit web interface with selectable operations

## Requirements

- Python 3.11 or newer
- Git

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/jemmziray-tech/calculator.git
   cd calculator
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   On Windows PowerShell, use:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Run the Project

### Command line

```bash
python calculator.py
```

### Streamlit web app

```bash
streamlit run app.py
```

Streamlit will print a local URL in the terminal. Open that URL in your browser to use the web interface.

## Project Structure

```text
.
├── app.py             # Streamlit web interface
├── calculator.py      # Calculation functions and CLI program
├── requirements.txt   # Python dependencies
└── .gitignore         # Files excluded from Git
```

## Git Practice Workflow

Use this project to practice a collaborative feature workflow:

1. Start from the latest `main` branch:

   ```bash
   git switch main
   git pull origin main
   ```

2. Create a descriptive feature branch:

   ```bash
   git switch -c add-percentage-operation
   ```

3. Make a change, then review and commit it:

   ```bash
   git status
   git add .
   git commit -m "Add percentage operation"
   ```

4. Push the branch to GitHub:

   ```bash
   git push -u origin add-percentage-operation
   ```

5. Open a pull request, ask your friend to review it, and merge it after approval.

6. Update your local `main` branch before starting the next task.

Good practice ideas include adding a new operation, improving error messages, writing tests, or updating the Streamlit interface.

## Learning Goals

This project is intentionally simple so you can focus on practicing:

- Branches and commits
- Pull requests and code review
- Resolving merge conflicts
- Working with a shared repository
- Python functions and basic application structure

## License

This project is for learning and practice.
