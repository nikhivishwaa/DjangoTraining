from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('register.html')

@app.route('/submit', methods=['POST'])
def submit():
    hindi = float(request.form.get('hindi'))
    maths = float(request.form.get('maths'))
    science = float(request.form.get('science'))
    english = float(request.form.get('english'))

    totalscore = maths + science + maths + english

    percentage = totalscore / 4



    # Process or store the data
    return redirect(url_for('result', score=percentage))

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


if __name__ == '__main__':
    app.run(debug=True)
