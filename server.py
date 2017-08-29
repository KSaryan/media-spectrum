from jinja2 import StrictUndefined
from flask import jsonify
from flask import (Flask, render_template, redirect, request, flash,
                   session, url_for, g)
from sqlalchemy import update
import json
# from datetime import datetime, timedelta, date
import requests
import re

import os
from functools import wraps
from screenshot import *
from subprocess import Popen, PIPE
from selenium import webdriver
import time


app = Flask(__name__)
app.secret_key = "ABC"



# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if g.current_user is None:
#             flash("Log in to access")
#             return redirect('/')
#         return f(*args, **kwargs)
#     return decorated_function


# @app.before_request
# def pre_process_all_requests():
#     """Setup the request context"""

#     user_id = session.get('user_id')
#     if user_id:
#         g.current_user = User.query.get(user_id)
#         g.logged_in = True
#         g.email = g.current_user.email
#         g.user_id = g.current_user.user_id
#         g.phone = g.current_user.phone
#     else:
#         g.logged_in = False
#         g.current_user = None
#         g.email = None

@app.route('/')
def display_homepage():
    """Displas hoempage"""
    return render_template('homepage.html')

@app.route('/get_time')
def get_time():
    now = time.time()

    return str(now)

@app.route('/word_cloud')
def show_word_cloud():
	return render_template('wordcloud.html')
# @app.route('/get_screenshot')
# def get_screenshot():
#     filename = request.args.get('url').rstrip('.com') + '.png'
#     return filename


  
if __name__ == "__main__":

    app.debug = True
    # connect_to_db(app)


    app.run(port=5000, host='0.0.0.0')

