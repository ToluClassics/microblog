from flask import render_template
from myapp import app
from myapp.forms import LoginForm


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

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title="Log in",form=form)