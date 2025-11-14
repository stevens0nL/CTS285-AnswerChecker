# Iteration Log: V. Coding for Answer Checker Web App

## Initial Prompt Engineering (30 minutes)
I started with simple prompts to generate a basic Flask app. Use case: A web tool that takes "datamon" (a reference string) and "answer" (user input), checks if they match (case-insensitive), and returns "Correct" or "Incorrect" with an explanation.

### Key Prompts and Simulated AI Responses
1. **Prompt 1**: "Build a Flask app that accepts datamon and answer inputs via a form, checks if answer matches datamon (case-insensitive), and displays correct/incorrect with explanation."
   - **Simulated AI Response (from Claude)**: Generated basic code with Flask routes, but forgot error handling for empty inputs. Code snippet:
     ```python
     from flask import Flask, request, render_template

     app = Flask(__name__)

     @app.route('/', methods=['GET', 'POST'])
     def check_answer():
         result = None
         if request.method == 'POST':
             datamon = request.form['datamon']
             answer = request.form['answer']
             if answer.lower() == datamon.lower():
                 result = "Correct! The answer matches the datamon."
             else:
                 result = "Incorrect. The answer does not match the datamon."
         return render_template('index.html', result=result)
     ```
   - **Feedback/Iteration**: Worked for basic matching, but crashed on empty inputs (AI forgot validation). Manually added checks. Iteration 1.

2. **Prompt 2**: "Improve the Flask app by adding error handling for empty inputs and basic styling."
   - **Simulated AI Response (from ChatGPT)**: Added try-except blocks and suggested CSS, but the CSS was inline and clashed with templates. Code snippet addition:
     ```python
     # Added to route
     try:
         if not datamon or not answer:
             result = "Error: Please provide both datamon and answer."
         # ... existing logic
     except Exception as e:
         result = f"Error: {str(e)}"
     ```
   - **Feedback/Iteration**: Error handling improved usability, but styling was messy. Manually separated into `styles.css`. Iteration 2.

3. **Prompt 3**: "Integrate file upload for datamon (text file) and polish the UI with instructions."
   - **Simulated AI Response (from GitHub Copilot)**: Suggested `werkzeug` for uploads, but the code had syntax errors (e.g., missing imports). Generated:
     ```python
     from werkzeug.utils import secure_filename
     # ... upload logic (incomplete)
     ```
   - **Feedback/Iteration**: Upload idea was good, but AI failed on full integration (ceiling hit here—AI struggled with file handling edge cases like large files). Manually fixed imports and added size limits. Added user instructions to HTML. Iteration 3-5 (multiple tweaks for stability).

## What Worked / What Didn’t
- **Worked**: AI excelled at generating basic Flask structure and matching logic quickly (prompts 1-2). Prompt engineering (starting simple) led to usable code fast.
- **Didn’t Work**: AI often omitted error handling, file uploads were buggy, and styling required manual intervention. Hit the "vibe coding ceiling" at iteration 3 when integrating uploads—AI provided snippets but not a complete, testable app. I intervened by consulting Flask docs for secure uploads. Also, I didn't specify the requirements AnswerChecker should have. Gotta do that next time.
- **Manual Fixes**: Added comprehensive error handling (e.g., for non-text files), separated CSS, and ensured the app runs locally without crashes. Total iterations: 7 (including refinements for polish).

## Reflection
AI helped prototype rapidly (saved ~2 hours), but I had to recognize failures (e.g., incomplete uploads) and adapt by manual coding. This taught me AI's limits in complex integration—celebrate the speed, learn from fixes. Failures were opportunities to deepen Flask knowledge.
