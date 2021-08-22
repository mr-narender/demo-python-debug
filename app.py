from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Home</h1>'


@app.route('/about')
def about():
    name = 'John'
    return f'<h1>About, {name}</h1>'


if __name__ == '__main__':
    app.run(debug=True)
