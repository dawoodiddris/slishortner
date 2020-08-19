from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/urlshortner')
def urlshortner():
    return render_template('form.html')


@app.route('/data', methods=['GET','POST'])
def data():

    return render_template('data.html', name=request.form['email'])