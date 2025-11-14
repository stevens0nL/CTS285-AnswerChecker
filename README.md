# Answer Checker Web App

A simple Flask-based web tool to check if a user-provided math solution is correct. Built using vibe coding with AI assistance.

## What It Does
- Accepts a "datamon" input (math problem, e.g., "2 + 3" or "x + 1 = 3", text or uploaded .txt file).
- Accepts an "answer" input (proposed solution, e.g., "5" or "2").
- Evaluates the math problem symbolically using sympy.
- Displays "Correct" or "Incorrect" with the computed result or solution.
- Handles errors (e.g., invalid math, empty inputs) smoothly, I guess.
- Basic UI with instructions for usability (and because I was lazy).

## How to Install Dependencies
1. Ensure Python ~3+ is installed.
2. Clone the repo and navigate to the directory.
3. Run: `pip install -r requirements.txt`

## How to Run the Application
1. Set environment: `export FLASK_APP=app.py` (or `set FLASK_APP=app.py` on Windows).
2. Run: `flask run`.
3. Open http://127.0.0.1:5000 in your browser.
4. Test with sample inputs (e.g., datamon: "2 + 3", answer: "5" → Correct; datamon: "x + 1 = 3", answer: "2" → Correct).

## Known Limitations
- Supports basic arithmetic and simple equations (e.g., linear); complex math (e.g., calculus) may fail.
- Only supports .txt uploads (max 1MB).
- Solutions are approximate for floats; exact for integers.
- Local-only; for deployment, use Gunicorn or Heroku. (AI told me this. Idk what it is)
- Styling is basic; not mobile-optimized.
