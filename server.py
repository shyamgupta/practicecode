from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello():
    my_name = request.args.get('name')
    my_color = request.args.get('color')
    return '{} {}'.format(my_name,my_color)

app.run(port=5000,debug=True)