''' How to integrated HTML with flask frameowrks'''
from flask import Flask , render_template
'''
It creates a instance of class  flask classs , which acts as  the WSGI application.
'''
## WSGI application instance
app = Flask(__name__)

@app.route("/") 
def welcome():
    return "<html><H1> Welcome to the flask web page with HTML 5 </H1></html>"
    

@app.route("/index", methods=['GET']) 
def home():   
    return render_template('index.html')
@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        mame = request.form['name']
        return f"Hello,{name}!"
    return render_template('form.html')


@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":  
    app.run(debug= True)