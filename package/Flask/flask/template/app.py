## Learning Flask - A Micro Web Framework for Python
from flask import Flask, request, render_template

'''
It creates an instance of class Flask, which acts as the WSGI application.
'''
## WSGI application instance
app = Flask(__name__)


@app.route("/")
def welcome():
    return "<html><h1>Welcome to the Flask web page with HTML5</h1></html>"


@app.route("/index", methods=['GET'])
def home():
    return render_template('index.html')


@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}!"
    return render_template('form.html')


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)