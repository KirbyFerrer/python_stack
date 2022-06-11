from flask import Flask, render_template
from help import generate_checkerboard
app = Flask(__name__)

@app.route('/')
def basic():
    result = generate_checkerboard(8, 8)
    return render_template('index.html', result = result)

@app.route('/<int:y>')
def basic_2(y):
    result = generate_checkerboard(8, y)
    return render_template('index.html', result = result)

@app.route('/<int:x>/<int:y>')
def basic_3(x, y):
    result = generate_checkerboard(x, y)
    return render_template('index.html', result = result)

if __name__ == '__main__':
    app.run(debug=True)