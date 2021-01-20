from flask import render_template
from myapp import app

@app.route("/")
@app.route("/index")

def index():
    user = {'username':'Odunayo'}
    posts = [
        {
            'author': {'username':'Jude'},
            'body':'Beautiful day in Portland!'
        },
        {
            'author': {'username':'Tolu'},
            'body':'Awful day in England!'
        }
    ]
    return render_template('index.html',title="Home",user=user,posts=posts)