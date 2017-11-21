from jinja2 import StrictUndefined
from flask import jsonify
from flask import (Flask, render_template, redirect, request, flash,
                   session, url_for, g)
from sqlalchemy import update
import json

import os
from functools import wraps
from subprocess import Popen, PIPE
from selenium import webdriver
import time
from count import count_words, count_one_word
from model import db, connect_to_db, User, Site, FaveSite
import ast

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
    """displays hoempage"""

    sites = Site.query.all()
    return render_template('homepage.html', sites=sites)


@app.route('/get_time')
def get_time():
    """returns current time"""

    now = time.time()

    return str(now)


@app.route('/word_frequency.json')
def get_frequent_words():
    """returns dictionary of most frequent words in a site"""

    url = request.args.get('url')
    site = Site.query.filter_by(url=url).first()
    frequency_dict = count_words(site)
    return jsonify(frequency_dict)


@app.route('/word_count.json')
def get_word_count():
    """returns how often a word shows up in chosen sites"""

    word = request.args.get('word')
    urls = ast.literal_eval(request.args.getlist('sites')[0])
    sites = []
    for url in urls:
        site = Site.query.filter_by(url=url).first()
        sites.append(site)
    count = count_one_word(word, sites)
    return jsonify(count)


@app.route('/stats/<site_name>')
def show_site_info(site_name):
    """returns site info page"""

    site = Site.query.filter_by(route_name=site_name).first()
    site_url = site.url
    sites = Site.query.all()
    return render_template('site-info.html', site_url=site_url, sites=sites)  
  
if __name__ == "__main__":

    app.debug = True
    connect_to_db(app)
    # def run_jobs(app):
    #     gh = threading.Thread(name='get_htmls', target=get_htmls)
    #     ms = threading.Thread(name='make_screenshots', target=make_screenshots)
    #     app = threading.Thread(name='app', target=app.run(port=5000, host='0.0.0.0'))
    #     app.start()
    #     gh.start()
    #     ms.start()

    # run_jobs(app)

    app.run(port=5000, host='0.0.0.0')

