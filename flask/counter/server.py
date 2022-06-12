from contextlib import redirect_stderr
from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = 'counter key'

@app.route('/')
def index():
    
    if 'counter_1' not in session:
        session['counter_1'] = 0
    
    return render_template('index.html')

@app.route('/counter/<int:counter>')
def man_counter(counter):
    session[f'counter_{counter}'] += 1

    return redirect('/')

@app.route('/reset')
def reset_counter():
    session.clear()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)