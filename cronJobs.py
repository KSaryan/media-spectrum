import schedule
import time
import urllib
import pickle
import threading
from html import *
from model import Site, db, connect_to_db

texts = {}


def get_htmls():
    sites = Site.query.all()

    for site in sites:
        print "Getting html"
        url = site.url
        html = urllib.urlopen(url).read()
        text = (text_from_html(html))
        site.html = text
        db.session.commit()


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


def run_jobs():

    gh = threading.Thread(name='get_htmls', target=get_htmls)
    ms = threading.Thread(name='make_screenshots', target=make_screenshots)
    gh.start()
    ms.start()


if __name__ == "__main__":
    from server import app
    connect_to_db(app)

    schedule.every(1).minutes.do(run_jobs)

    while True:
        schedule.run_pending()
        time.sleep(1)
