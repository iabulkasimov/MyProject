from flask import Flask

app = Flask(__name__)

@app.route("/")
def head():
    return "Hello World!"

@app.route('/abc')
def head1():
    return "Second Page Hello World!"

@app.route('/third/abc')
def head2():
    return "Third Page Hello World!"

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id of this pae is {id}'

if __name__ == '__main__':
    app.run(debug=True)
