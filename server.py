from jinja2 import StrictUndefined
from flask import jsonify
from flask import (Flask, render_template, redirect, request, flash,
                   session, url_for, g)
from sqlalchemy import update
import json
# from datetime import datetime, timedelta, date
# import requests
# import re

import os
from functools import wraps
# from screenshot import *
from subprocess import Popen, PIPE
from selenium import webdriver
import time
from count import count_words, count_one_word
from sites import SITES_TO_VISIT
# from cronJobs import get_htmls, make_screenshots
# import threading
# import schedule


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
    return render_template('homepage.html', sites=SITES_TO_VISIT)

@app.route('/get_time')
def get_time():
    now = time.time()

    return str(now)

# @app.route('/word_cloud')
# def show_word_cloud():
# 	return render_template('wordcloud.html', sites=SITES_TO_VISIT)

@app.route('/word_cloud.json')
def get_word_cloud_info():
    key = request.args.get('url')
    frequency_dict = count_words(key)
    print frequency_dict
    return jsonify(frequency_dict)
# @app.route('/get_screenshot')
# def get_screenshot():
#     filename = request.args.get('url').rstrip('.com') + '.png'
#     return filename

# @app.route('/word_count')
# def show_word_count():
#     return render_template('wordcount.html', sites=SITES_TO_VISIT)


@app.route('/word_count.json')
def get_word_count():
    word = request.args.get('word')
    sites = json.loads(request.args.get('sites'))
    count = count_one_word(word, sites)
    return jsonify(count)


# @app.route('/grid')
# def show_grid():
#     return render_template('grid.html', sites=SITES_TO_VISIT)


# @app.route('/example')
# def show_example():
#     return render_template('example.html', sites=SITES_TO_VISIT)

@app.route('/stats/<site_name>')
def show_site_info(site_name):
    for site in SITES_TO_VISIT:
        if SITES_TO_VISIT[site]['route_name'] == site_name:
            site_url = site
    return render_template('site-info.html', site_url=site_url, sites=SITES_TO_VISIT)  
  
if __name__ == "__main__":

    app.debug = True
    # connect_to_db(app)
    # def run_jobs(app):
    #     gh = threading.Thread(name='get_htmls', target=get_htmls)
    #     ms = threading.Thread(name='make_screenshots', target=make_screenshots)
    #     app = threading.Thread(name='app', target=app.run(port=5000, host='0.0.0.0'))
    #     app.start()
    #     gh.start()
    #     ms.start()

    # run_jobs(app)

    app.run(port=5000, host='0.0.0.0')

