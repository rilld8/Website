from flask import render_template
from app import app


@app.route('/')
@app.route('/index')

def index():
    user = {'nickname': 'Karol'}
    return render_template('Index.html', title='Karol Sz.', user=user)
