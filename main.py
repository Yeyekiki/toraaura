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
    return render_template('shop.html', logged_in=session.get('logged_in'))

@app.route('/leon')
def leon():
    return render_template('details.html', logged_in=session.get('logged_in'), title="LEON, painting", image="leon.jpeg", description="This is a painting of the infamous poster of Luc Besson's masterpiece 'Leon: The Professional'. We can see Leon (Jean Reno) with sunglasses staring at NY's skyline. If you are interested in learning more about or purchasing this piece, please contact me for further information.")

@app.route('/kanja')
def kanja():
    return render_template('details.html', logged_in=session.get('logged_in'), title="Kanja, picture", image="hippie.jpeg", description="This is a picture of Kanja, the second greatest artist in the world (currently).")

@app.route('/bath')
def bath():
    return render_template('details.html', logged_in=session.get('logged_in'), title="The Bath, painting", image="bath.jpeg", description="This is a painting inspired by a picture taken by the talented Sarah Babah.")

@app.route('/hall')
def hall():
    return render_template('details.html', logged_in=session.get('logged_in'), title="Unusual Warmth, picture", image="hall.jpeg", description="This is a film picture taken in a cold and isolated hallway that was illuminated by sunlight.")

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




