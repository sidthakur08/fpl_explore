from flask import render_template

from flask import current_app as app
from fpl.dashboard import keeper, defender, attacker

@app.route('/')
@app.route('/home')
def landing_page():
    return render_template('index.html')

@app.route('/keeper/')
def keeper_dash():
    return render_template('frame.html',dash_url = keeper.URL_BASE)

@app.route('/defender/')
def defender_dash():
    return render_template('frame.html',dash_url = defender.URL_BASE)

@app.route('/attacker/')
def attacker_dash():
    return render_template('frame.html',dash_url = attacker.URL_BASE)