from flask import Flask,url_for,render_template


app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template('homepage.html')


@app.route("/aboutpage")
def AboutPage():
    return render_template('ABOUTPAGE.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')


@app.route("/signIn")
def signIn():
    return render_template('login.html')