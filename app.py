from flask import Flask, render_template
from database import get_data
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/addtodo')
def addtodo():
    data=get_data()
    return render_template('addtodo.html', data=data)
if __name__=="main":
    app.run()