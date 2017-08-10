from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/scores')
def print_scores():
    a_dictionary = {'John':45,'Mary':90,'Beth':78}
    return render_template('index.html',scores=a_dictionary)

app.run(port=5000,debug=True)


@app.route('/add/<int:num1>/<int:num2>')
def add_integers():
    number1=request.args.get('num1')
    number2=request.args.get('num2')
    return render_template('add.html',number1,number2)