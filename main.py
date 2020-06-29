from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

@app.route('/')
def home():
    return render_template('index.html', logged_in=session.get('logged_in'))

@app.route('/shop')
def shop():
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(Artwork)
    artworks = query.all()
    return render_template('shop.html', logged_in=session.get('logged_in'), artworks=artworks)

@app.route('/details/<name>')
def details(name):
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(Artwork).filter(Artwork.path.in_([name]))
    result = query.first()
    print(result)
    return render_template('details.html', logged_in=session.get('logged_in'), title=result.title, image=result.image, description=result.description)


@app.route('/donate')
def donate():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('paypal.html')


@app.route('/login', methods=['GET', 'POST'])
def do_admin_login():
    if request.method == 'POST':
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])

        Session = sessionmaker(bind=engine)
        s = Session()
        query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
        result = query.first()

        if not result == None:
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            flash('wrong password!')
        return home()

    elif request.method == 'GET':
        return render_template('login.html')


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()




