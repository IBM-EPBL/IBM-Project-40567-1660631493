from flask import Blueprint, render_template

blue_print = Blueprint("print", _name_)

@blue_print.route('/')
def home():
    return render_template('index.html')