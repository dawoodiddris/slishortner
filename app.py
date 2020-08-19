from flask import Flask, render_template, request, session

app = Flask(__name__)

app.secret_key = 'fghjklkjhgfdfghjktrertyuytf'

@app.route('/')
def home():
    return render_template('home.html', emails=session.keys())

@app.route('/urlshortner')
def urlshortner():
    return render_template('form.html')


@app.route('/data', methods=['GET','POST'])
def data():
    session[request.form['email']] = True
    return render_template('data.html', email=request.form['email'])