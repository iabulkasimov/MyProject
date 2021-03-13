from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return render_template('index.html', number1 = 12, number2 = 20)

@app.route('/calculator/<int:number1>/<int:number2>/<string:operator>')
def number(number1, number2, operator):
    # variable1, variable2 = 23, 45
    if operator == '+':
        return render_template('body.html', num1=number1, num2=number2, mult=number1 + number2, opt=operator)
    if operator == '-':
        return render_template('body.html', num1=number1, num2=number2, mult=number1 - number2, opt=operator)
    if operator == '*':
        return render_template('body.html', num1=number1, num2=number2, mult=number1 * number2, opt=operator)
    if operator == '÷':
        return render_template('body.html', num1=number1, num2=number2, mult=number1 / number2, opt=operator)

if __name__ == '__main__':
    app.run(debug=True)