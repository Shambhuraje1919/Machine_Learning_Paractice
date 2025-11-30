from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/result', methods=['POST'])
def check_result():
    input_value = request.form.get('input')
    
    if input_value == 'correct':
        result = 'Congratulations! You passed!'
    else:
        result = 'Sorry, you failed!'
    
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run()