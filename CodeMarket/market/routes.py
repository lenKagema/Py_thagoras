from flask import render_template
from . import app
from .models import Item


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)
