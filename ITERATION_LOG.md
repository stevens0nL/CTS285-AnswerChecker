# Iteration Log: V. Coding for Answer Checker Web App

## Initial Prompt Engineering (30 minutes)
I started with simple prompts to generate a basic Flask app. Use case: A web tool for checking math answers in two steps—first input equation, compute solution, then input answer and check. Includes sessions (5/10/20 limits), a practice list (up to 10 equations), CSV logging, and download/clear options.

### Key Prompts and Simulated AI Responses
1. **Prompt 1**: "Build a Flask app with sessions for two-step math checking: first input equation, compute solution, then input answer and check with simple feedback ('correct' or 'incorrect with answer'). Add session limits (5/10/20 inputs) and a prompt to continue or reset."
   - **Simulated AI Response (from Claude)**: Generated basic session code with Flask-Session, but forgot to handle equation computation storage. Code snippet:
     ```python
     from flask import Flask, session
     app = Flask(__name__)
     app.secret_key = 'key'
     # Basic route with session count
     ```
   - **Feedback/Iteration**: Worked for session basics, but AI missed solution pre-computation. Manually added sympy logic and session storage. Iteration 1.

2. **Prompt 2**: "Add a practice list (up to 10 equations in memory) and CSV logging for equations, solutions, and wrong user inputs."
   - **Simulated AI Response (from ChatGPT)**: Suggested csv module and list append, but the list wasn't limited or integrated with sessions. Code snippet:
     ```python
     import csv
     practice_list = []
     # ... logging logic
     ```
   - **Feedback/Iteration**: Logging improved, but AI forgot list limits and session ties. Manually capped list at 10 and linked to sessions. Iteration 2.

3. **Prompt 3**: "Add download/clear options for CSV after session, modal popup for feedback, and UI for session selection and count display."
   - **Simulated AI Response (from GitHub Copilot)**: Provided HTML modal and download links, but JS for prompts was incomplete. Generated:
     ```python
     # Flask route for download
     @app.route('/download')
     def download_csv():
         return send_file('equations_log.csv', as_attachment=True)
     ```
   - **Feedback/Iteration**: Download worked, but AI hit the ceiling with full session flow and list management—struggled with continuing/resetting sessions. Manually fixed with JS prompts and list pruning. Iteration 3-6 (multiple for integration).

## What Worked / What Didn’t
- **Worked**: AI excelled at generating session basics and CSV logging (prompts 1-2). Prompt engineering led to usable code fast.
- **Didn’t Work**: AI often omitted limits, list caps, and full session flow. Hit the "vibe coding ceiling" at iteration 3 with modals and download—provided snippets but not integrated logic. I intervened by consulting Flask docs for sessions and JS for modals.
- **Manual Fixes**: Added session limits, list management, modal JS, and ensured feedback is simple. Total iterations: 9 (including refinements).

## Reflection
AI helped prototype sessions and logging rapidly (saved ~2 hours), but I had to recognize failures (e.g., incomplete flows) and adapt manually. This taught me AI's limits in stateful apps—celebrate the speed, learn from fixes. Failures were opportunities to deepen Flask session knowledge.
