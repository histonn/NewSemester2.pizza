from flask import Flask, render_template
app = Flask(__name__)

test_name = "Python project"
max_score = 100

students = [
    {'name': 'John', 'score': 100},
    {'name': 'Vika', 'score': 93},
    {'name': 'Katya', 'score': 34},
    {'name': 'Vitya', 'score': 45}
]


@app.route('/results')
def results():
    contex = {
        'title': 'Result',
        'students': students,
        'test_name': test_name,
        'max_score': max_score
    }
    return render_template('results.html', **contex)


test_name2 = 'Portfolio'
now = 2023
projects = [
    {'name': 'Telegram bot', 'when': 2024},
    {'name': 'Game', 'when': 2023},
    {'name': 'Website', 'when': 2024}
]


@app.route('/myproject')
def portfolio():
    contex2 = {
        'title2': 'Myprojects',
        'projects': projects,
        'test_name2': test_name2,
        'now': now
    }
    return render_template('myproject.html', **contex2)


@app.route('/')
def index():
    return render_template('base.html', title='Jinja_Test')
















if __name__ == '__main__':
    app.run(debug=True)



