from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def head():
    first = 'This is my first conditions!'
    return render_template('index.html', message = first)

@app.route('/ikbal')
def elnur():
    name = [ 'Serdar,', 'Orlando', 'Noble', 'Callahan']
    return render_template('body.html', object = name)

@app.route('/calculator/<int:number1>/<int:number2>/<string:operator>')
def number(number1, number2, operator):
    math_operators = ['+', '-', '*', '÷']
    return render_template('calculator.html', num1=number1, num2=number2, opt=operator, for_loop = math_operators)

if __name__==('__main__'):
    app.run(debug=True)