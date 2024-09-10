from flask import Flask, redirect, url_for

app = Flask(__name__) # giving name to app , it is entry point

@app.route('/success/<int:score>')
def success(score):
    return f'<h1>my 12th score is : {score}</h1><h2 style="color:green;">Pass</h2>'

@app.route('/fail/<int:score>')
def fail(score):
    return f'<h1>my 12th score is : {score}</h1><h2 style="color:red;">Fail</h2>'

@app.route('/result/<int:score>/')
def result(score):
    url = 'fail'
    if score >= 33:
        url = 'success'

    print(url)
        
    return redirect(url_for(url, score=score))

@app.route('/ranges/<int:num>/')
def ranges(num):
    url = 'firsthundred'
    if num >= 1 and num <= 100:
        url = 'firsthundred'
    elif num >= 101 and num <= 200:
        url = 'secondhundred'
    elif num >= 201 and num <= 300:
        url = 'thirdhundred'
        
    return redirect(url_for(url, num=num))

@app.route('/firsthundred/<int:num>')
def firsthundred(num):
    return f'<h1>the given no. "{num}" is ranges beteen 1 to 100</h1>'

@app.route('/secondhundred/<int:num>')
def secondhundred(num):
    return f'<h1>the given no. "{num}" is ranges beteen 101 to 200</h1>'

@app.route('/thirdhundred/<int:num>')
def thirdhundred(num):
    return f'<h1>the given no. "{num}" is ranges beteen 201 to 300</h1>'

if __name__ == '__main__':
    app.run(debug=True) # it is exit point