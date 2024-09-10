from flask import Flask

app = Flask(__name__)


@app.route('/')
def Welcome():
    return '<h1>Hello from Flask! Do You Love to Have Coffee</h1>'

@app.route('/home/')
def home():
    return '<h1>Welcome to SISTec Bhopal</h1>'

@app.route('/api/')
def api():
    return {'status': 'ok', 'title': 'this is an api'}


if __name__ == '__main__':
    app.run(debug=True)