from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Geremy Good'}  # fake user
    events = [  # fake array of events
        {
            'host': {'name': 'Host 1'},
            'name': 'Initial Event'
        },
        {
            'host': {'name': 'Host 2'},
            'name': 'Event Two: The second event'
        }
    ]
    return render_template('index.html',
                            title='home',
                            user=user,
                            events=events)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash('Login requested for OpenID-"%s"m remember_me=%s' %
            (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')

    return render_template('login.html',
                            title='Sign In',
                            form=form,
                            providers=app.config['OPENID_PROVIDERS'])
