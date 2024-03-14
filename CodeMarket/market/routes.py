from flask import render_template, redirect, url_for
from . import app, db
from .models import Item, User
from .forms import RegisterForm


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route('/register')
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))

    return render_template('register.html', form=form)
