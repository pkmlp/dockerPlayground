
"""
This python-script runs the HelloFlask application
"""

from datetime import datetime
from flask import Flask, render_template, flash, request, redirect, url_for, session

from functools import wraps
import sqlite3 as db

from passlib.apps import custom_app_context as password_hash


app = Flask(__name__)

app.secret_key = 'flash_requires_a_secret_key'


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("Dashboard is available for logged in users only")
            return redirect(url_for('login'))

    return wrap


"""
routes and views for the flask application.
"""


@app.route('/')
@app.route('/index/')
def index():
    """Renders the home page."""

    try:
        return render_template(
            'index.html',
            title='Home',
            year=datetime.now().year
        )
    except Exception as e:
        return render_template(
            "500.html",
            message=str(e)
        )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    try:
        return render_template(
            'contact.html',
            title='Contact',
            year=datetime.now().year,
            message='Feedbacks, Comments, Suggestions are very welcome'
        )
    except Exception as e:
        return render_template(
            "500.html",
            message=str(e)
        )


@app.route('/about')
def about():
    """Renders the about page."""
    try:
        return render_template(
            'about.html',
            title='About',
            year=datetime.now().year,
            message='This Website - a live example of a Website with Python, Flask and Bootstrap'
        )
    except Exception as e:
        return render_template(
            "500.html",
            message=str(e)
        )


@app.route('/dashboard')
@login_required
def dashboard():
    """Renders the dashboard page."""
    try:
        return render_template(
            'dashboard.html',
            title='Dashboard',
            year=datetime.now().year,
            message='All Source Codes of this Website'
        )
    except Exception as e:
        return render_template(
            "500.html",
            message=str(e)
        )


@app.route('/login/', methods=["GET", "POST"])
def login():
    """Renders the login page."""
    if 'logged_in' in session:
            flash("You are already logged in as: " + session['username'])
            return redirect(url_for('dashboard'))

    error = ''
    try:
        if request.method == "POST":

            attempted_username = request.form['username']
            attempted_password = request.form['password']

            userDataUsername = ""
            userDataPassword = ""

            connection = db.connect("/usr/src/app/HelloFlask.db")
            cursor = connection.cursor()

            sqlStatement = "SELECT * FROM user WHERE username = ?"
            userData = cursor.execute(sqlStatement, [attempted_username])

            for user in userData:
                userDataUsername = user[2]
                userDataPassword = user[3]

            cursor.close()
            connection.close()

            if attempted_username == userDataUsername and password_hash.verify(attempted_password, userDataPassword):
                session['logged_in'] = True
                session['username'] = userDataUsername
                return redirect(url_for('dashboard'))

            else:
                error = "Invalid Username or Password  -  Please try again."

        return render_template("login.html", error=error)

    except Exception as e:
        return render_template("login.html", error=str(e))


@app.route('/logout')
@login_required
def logout():
    """clears the session and redirects to the index page."""
    try:
        session.clear()
        return redirect(url_for('index'))
    except Exception as e:
        return render_template(
            "500.html",
            message=str(e)
        )


@app.route('/register/', methods=["GET", "POST"])
def register():
    """Renders the register page."""

    error = ''
    try:

        if request.method == "POST":

            if 'logged_in' in session:
                session.clear()

            attempted_email = request.form['email']
            attempted_username = request.form['username']
            attempted_password = request.form['password']
            attempted_confirm = request.form['confirm']

            connection = db.connect("/usr/src/app/HelloFlask.db")
            cursor = connection.cursor()

            userDataUsername = ""
            sqlStatement = "SELECT * FROM user WHERE username = ?"
            userData = cursor.execute(sqlStatement, [attempted_username])

            for user in userData:
                userDataUsername = user[2]

            cursor.close()
            connection.close()

            if attempted_username == userDataUsername:
                error = 'Username already exists  -  Please try another one.'
                return render_template("register.html", error=error)

            if attempted_password != attempted_confirm:
                error = 'Password does not match Confirmation  -  Please check.'
                return render_template("register.html", error=error)

            hashed_Password = password_hash.encrypt(attempted_password)

            connection = db.connect("/usr/src/app/HelloFlask.db")
            cursor = connection.cursor()

            sqlStatement = "INSERT INTO user (email, username, password) VALUES (?, ?, ?)"
            cursor.execute(sqlStatement, (attempted_email, attempted_username, hashed_Password))

            cursor.close()
            connection.commit()
            connection.close()

            session['logged_in'] = True
            session['username'] = attempted_username
            return redirect(url_for('dashboard'))

        if 'logged_in' in session:
            flash("You are already logged in as: " + session['username'])

        return render_template("register.html", error=error)

    except Exception as e:
        return render_template('register.html', error=str(e))


@app.route('/delete')
@login_required
def delete():
    """deletes actual account."""
    try:
        connection = db.connect("/usr/src/app/HelloFlask.db")
        cursor = connection.cursor()

        sqlStatement = "DELETE FROM user WHERE username = '%s'" %session['username']
        cursor.execute(sqlStatement)

        cursor.close()
        connection.commit()
        connection.close()

        session.clear()
        return redirect(url_for('index'))

    except Exception as e:
        return render_template(
            "500.html",
            message=str(e)
        )


@app.errorhandler(404)
def page_not_found(e):
    """Renders the not found page."""
    try:
        return render_template("404.html")

    except Exception as e:
        return render_template("500.html", message=str(e))


@app.errorhandler(405)
def method_not_allowed(e):
    """Renders the not found page."""
    try:
        return render_template("405.html")

    except Exception as e:
        return render_template("500.html", message=str(e))


if __name__ == '__main__':
    app.run(host="0.0.0.0")


