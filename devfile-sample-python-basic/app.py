from flask import Flask, render_template
from waitress import serve

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

# Hello to name
@app.route('/hello/<name>')
def say_hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    serve(app, host='10.64.242.70', port=8000)
    # serve(app)
