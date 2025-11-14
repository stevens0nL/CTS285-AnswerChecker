from flask import Flask, request, render_template, session, send_file, flash, redirect, url_for
from sympy import sympify, solve, Eq
import csv
import os
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

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'step' not in session:
        session['step'] = 'select_limit'
        session['count'] = 0
        session['limit'] = 0
        session['equation'] = ''
        session['solution'] = ''
    
    if request.method == 'POST':
        if session['step'] == 'select_limit':
            session['limit'] = int(request.form['limit'])
            session['step'] = 'input_equation'
            return redirect(url_for('index'))
        
        elif session['step'] == 'input_equation':
            equation = request.form['equation'].strip()
            try:
                expr = sympify(equation)
                if '=' in equation:
                    left, right = equation.split('=', 1)
                    eq = Eq(sympify(left), sympify(right))
                    solutions = solve(eq)
                    session['solution'] = str(solutions[0]) if solutions else 'No solution'
                else:
                    session['solution'] = str(float(expr))
                session['equation'] = equation
                session['step'] = 'input_answer'
                # Add to practice list if under 10
                if len(practice_list) < 10:
                    practice_list.append(equation)
                return redirect(url_for('index'))
            except Exception as e:
                flash(f"Error: Invalid equation. {str(e)}")
        
        elif session['step'] == 'input_answer':
            answer = request.form['answer'].strip()
            correct = session['solution']
            session['count'] += 1
            is_correct = answer == correct
            feedback = "This answer is correct" if is_correct else f"This answer is incorrect. The answer is {correct}."
            
            # Log to CSV if wrong
            if not is_correct:
                with open(CSV_FILE, 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([datetime.now(), session['equation'], correct, answer])
            
            # Check session limit
            if session['count'] >= session['limit']:
                session['step'] = 'session_end'
            else:
                session['step'] = 'input_equation'
            
            return render_template('index.html', feedback=feedback, modal=True)
    
    return render_template('index.html', practice_list=practice_list)

@app.route('/continue_session', methods=['POST'])
def continue_session():
    session['step'] = 'input_equation'
    return redirect(url_for('index'))

@app.route('/new_session', methods=['POST'])
def new_session():
    session.clear()
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
            expr = sympify(session['equation'])
            if '=' in session['equation']:
                left, right = session['equation'].split('=', 1)
                eq = Eq(sympify(left), sympify(right))
                solutions = solve(eq)
                session['solution'] = str(solutions[0]) if solutions else 'No solution'
            else:
                session['solution'] = str(float(expr))
            session['step'] = 'input_answer'
        except:
            flash("Error loading practice equation.")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
