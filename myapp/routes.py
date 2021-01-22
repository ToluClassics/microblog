from werkzeug.urls import url_parse
from flask import render_template, flash, redirect,url_for, request
from myapp import app
from myapp.forms import LoginForm
from myapp.models import User
from flask_login import login_user, current_user,logout_user, login_required


@app.route("/")
@app.route("/index")
@login_required
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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('invalid sign in credentials')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc !='':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html',title="Log in",form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))