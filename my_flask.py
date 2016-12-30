from flask import Flask

app = Flask(__name__)

@app.route('/')
def first():
    return 'first test'

@app.route('/a')
def a():
    return 'a'

if __name__ == '__main__':
    app.run()