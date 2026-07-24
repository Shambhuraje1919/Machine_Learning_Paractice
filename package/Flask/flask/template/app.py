## Learning Flask - A Micro Web Framework for Python
from flask import Flask

'''
It creates an instance of class Flask, which acts as the WSGI application.
'''
## WSGI application instance
app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to Flask!"


if __name__ == "__main__":
    app.run(debug=True)