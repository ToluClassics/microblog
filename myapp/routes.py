from flask import render_template, flash, redirect,url_for
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

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('login'))
    return render_template('login.html',title="Log in",form=form)