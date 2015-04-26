from flask import render_template
from app import app

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
