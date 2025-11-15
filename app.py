from flask import Flask, request, render_template, session, send_file, flash, redirect, url_for
from sympy import sympify, solve, Eq
import csv
import os
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # For sessions

CSV_FILE = 'equations_log.csv'

# Initialize CSV if not exists
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Timestamp', 'Equation', 'Correct Solution', 'User Input (if wrong)'])

practice_list = []  # In-memory list for up to 10 equations

def generate_random_equation():
    """Generate a simple PEMDAS equation."""
    ops = ['+', '-', '*', '/']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    num3 = random.randint(1, 10)
    op1 = random.choice(ops)
    op2 = random.choice(ops)
    equation = f"{num1}{op1}{num2}{op2}{num3}"
    try:
        solution = str(float(sympify(equation)))
        return equation, solution
    except:
        return generate_random_equation()  # Retry if invalid

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'step' not in session:
        session['step'] = 'select_limit'
        session['count'] = 0
        session['limit'] = 0
        session['equation'] = ''
        session['solution'] = ''
        session['mode'] = 'regular'  # 'regular' or 'practice'
        session['practice_equations'] = []
        session['practice_solutions'] = []
        session['practice_index'] = 0
        session['practice_correct'] = 0
    
    feedback = None
    show_modal = False
    
    if request.method == 'POST':
        if session['step'] == 'select_limit' or 'change_limit' in request.form:
            session['limit'] = int(request.form['limit'])
            session['step'] = 'input_equation'
            return redirect(url_for('index'))
        
        elif session['step'] == 'input_equation':
            equation = request.form['equation'].strip().replace(' ', '')
            try:
                if '=' in equation:
                    left, right = equation.split('=', 1)
                    eq = Eq(sympify(left), sympify(right))
                    solutions = solve(eq)
                    session['solution'] = str(solutions[0]) if solutions else 'No solution'
                else:
                    expr = sympify(equation)
                    session['solution'] = str(float(expr))
                session['equation'] = equation
                if session['mode'] == 'practice':
                    session['practice_equations'].append(equation)
                    session['practice_solutions'].append(session['solution'])
                    if len(session['practice_equations']) >= 10:
                        session['step'] = 'practice_start'
                        return redirect(url_for('index'))
                    return redirect(url_for('index'))
                else:
                    session['step'] = 'input_answer'
                    if len(practice_list) < 10:
                        practice_list.append(equation)
                return redirect(url_for('index'))
            except Exception as e:
                flash(f"Error: Invalid equation. {str(e)}")
        
        elif session['step'] == 'input_answer':
            answer = request.form['answer'].strip()
            correct = session['solution']
            session['count'] += 1
            
            try:
                is_correct = abs(float(answer) - float(correct)) < 1e-6
            except ValueError:
                is_correct = answer == correct
            
            feedback = "This answer is correct" if is_correct else f"This answer is incorrect. The answer is {correct}."
            show_modal = True
            
            if not is_correct:
                with open(CSV_FILE, 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([datetime.now(), session['equation'], correct, answer])
            
            if session['count'] >= session['limit']:
                session['step'] = 'session_end'
            else:
                session['step'] = 'input_equation'
        
        elif session['step'] == 'practice_solve':
            answer = request.form['answer'].strip()
            correct = session['practice_solutions'][session['practice_index']]
            try:
                is_correct = abs(float(answer) - float(correct)) < 1e-6
            except ValueError:
                is_correct = answer == correct
            
            if is_correct:
                session['practice_correct'] += 1
            feedback = "Correct!" if is_correct else f"Incorrect. Answer: {correct}"
            flash(feedback)
            
            session['practice_index'] += 1
            if session['practice_index'] >= len(session['practice_equations']):
                session['step'] = 'practice_end'
            return redirect(url_for('index'))
    
    # Prepare practice list with indices for template
    practice_list_with_idx = list(enumerate(practice_list))
    
    return render_template('index.html', feedback=feedback, show_modal=show_modal, practice_list_with_idx=practice_list_with_idx)

@app.route('/start_practice', methods=['POST'])
def start_practice():
    session['mode'] = 'practice'
    session['step'] = 'input_equation'
    session['practice_equations'] = []
    session['practice_solutions'] = []
    return redirect(url_for('index'))

@app.route('/practice_start', methods=['POST'])
def practice_start():
    if not session['practice_equations']:
        # Generate random equations if none submitted
        for _ in range(10):
            eq, sol = generate_random_equation()
            session['practice_equations'].append(eq)
            session['practice_solutions'].append(sol)
    session['step'] = 'practice_solve'
    session['practice_index'] = 0
    session['practice_correct'] = 0
    return redirect(url_for('index'))

@app.route('/continue_session', methods=['POST'])
def continue_session():
    session['step'] = 'input_equation'
    return redirect(url_for('index'))

@app.route('/new_session', methods=['POST'])
def new_session():
    session.clear()
    return redirect(url_for('index'))

@app.route('/exit', methods=['POST'])
def exit_app():
    session.clear()
    return render_template('exit.html')

@app.route('/change_limit', methods=['POST'])
def change_limit():
    session['step'] = 'select_limit'
    return redirect(url_for('index'))

@app.route('/download_csv')
def download_csv():
    return send_file(CSV_FILE, as_attachment=True)

@app.route('/clear_csv', methods=['POST'])
def clear_csv():
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Timestamp', 'Equation', 'Correct Solution', 'User Input (if wrong)'])
    flash("History cleared.")
    return redirect(url_for('index'))

@app.route('/practice/<int:idx>')
def practice(idx):
    if 0 <= idx < len(practice_list):
        session['equation'] = practice_list[idx]
        try:
            if '=' in session['equation']:
                left, right = session['equation'].split('=', 1)
                eq = Eq(sympify(left), sympify(right))
                solutions = solve(eq)
                session['solution'] = str(solutions[0]) if solutions else 'No solution'
            else:
                expr = sympify(session['equation'])
                session['solution'] = str(float(expr))
            session['step'] = 'input_answer'
        except:
            flash("Error loading practice equation.")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)