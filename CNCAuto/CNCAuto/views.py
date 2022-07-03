"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from CNCAuto import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/specials')
def specials():
    """Renders the about page."""
    return render_template(
        'specials.html',
        title='Specials',
        year=datetime.now().year,
        message='special things here'
    )

@app.route('/shop')
def shop():
    """Renders the about page."""
    return render_template(
        'shop.html',
        title='Shop',
        year=datetime.now().year,
        message='shop things here'
    )


@app.route('/bookOnline')
def bookOnline():
    """Renders the about page."""
    return render_template(
        'bookOnline.html',
        title='Book Online',
        year=datetime.now().year,
        message='book online things here'
    )

@app.route('/bookingsCheckout')
def bookingsCheckout():
    """Renders the about page."""
    return render_template(
        'bookingsCheckout.html',
        title='Bookings Checkout',
        year=datetime.now().year,
        message='Bookings Checkout things here'
    )

