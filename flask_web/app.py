from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile/<int:ID>')
def wait(ID):
    return '<h1>hi im %s'%ID


app.run(debug=True)