## Learning Flask - A Micro Web Framework for Python
from flask import Flask
'''
It creates a instance of class  flask classs , which acts as  the WSGI application.
'''
## WSGI application instance
app = Flask(__name__)

@app.route("/") 
def welcome():
/*************  ✨ Windsurf Command ⭐  *************/
/*******  b0382827-bce4-4443-8be1-93e679b292ca  *******/
    return "Wlcome to this home , this the future data scentist  sam bossss first web page using python flask framework"

@app.route("/index") 
def home():
    return "Wlcome to this home , this the future data scentist "
if __name__ == "__main__":   ## Entry point of the application
    app.run(debug= True)
    