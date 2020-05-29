from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/leon')
def leon():
    return render_template('leondetails.html')

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


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)

