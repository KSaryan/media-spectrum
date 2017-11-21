import schedule
import time
import urllib2
import pickle
import threading
from html import *
from model import Site, db, connect_to_db
import requests
import cookielib


def get_htmls():
    sites = Site.query.all()

    for site in sites:
        print "Getting html"
        url = site.url

        try:
            html = requests.get(url).text
            html_lst = html.split('\x00')
            html_str = "".join(html_lst)
            text = (text_from_html(html_str))
            site.html = text
            db.session.commit()

        except Exception as inst:
            print type(inst)
            print inst.args
            print inst 
            print "I'm a problem"
            print url


from screenshot import *

def make_screenshots():
    print "Getting screenshot"

    sites = Site.query.all()

    sites = [get_screen_shot(
        url= site.url, filename=site.pic_name, path='./static/img',
        crop=True, crop_replace=False,
        thumbnail=True, thumbnail_replace=False,
        thumbnail_width=500, thumbnail_height=600,
        ) for site in sites]


# def run_jobs():

#     gh = threading.Thread(name='get_htmls', target=get_htmls)
#     ms = threading.Thread(name='make_screenshots', target=make_screenshots)
#     gh.start()
#     ms.start()

def run_jobs():
    get_htmls()
    make_screenshots()



if __name__ == "__main__":

    schedule.every(60).minutes.do(run_jobs)
    from server import app
    connect_to_db(app)
    while True:   
        schedule.run_pending()
        time.sleep(1)

    # run_jobs()

