# Math Answer Checker Web App

A simple Flask-based web tool to check if a user-provided math solution is correct. Built using vibe coding with AI assistance. Features two-step input, session limits, a practice list, and CSV history.

## What It Does
- **Two-Step Process**: Input equation first (solution computed), then input answer for checking.
- **Feedback**: Simple popup: "This answer is correct" or "This answer is incorrect. The answer is [correct]."
- **Sessions**: Choose 5, 10, or 20 inputs per session. Prompt to continue or reset when limit reached. Shows input count.
- **Practice List**: Stores up to 10 equations in memory for practice (no file save). Download CSV for more.
- **Database**: CSV file (`equations_log.csv`) logs equations, solutions, wrong user inputs, and timestamps.
- **Download/Clear**: After session, download history or clear the CSV.
- Handles errors (e.g., invalid math) gracefully.

## How to Install Dependencies
1. Ensure Python 3.8+ is installed.
2. Clone this repo and navigate to the directory.
3. Run: `pip install -r requirements.txt`

## How to Run the Application
1. Set environment: `export FLASK_APP=app.py` (or `set FLASK_APP=app.py` on Windows).
2. Run: `flask run`.
3. Open http://127.0.0.1:5000 in your browser.
4. Select session limit, input equation, then answer. Practice from list or download history.

## Known Limitations
- Supports basic arithmetic and simple equations; complex math may fail.
- Sessions are browser-based (cleared on refresh).
- Practice list limited to 10; use CSV for more.
- Local-only; for deployment, use Gunicorn or Heroku.
- Styling is basic; not mobile-optimized.
