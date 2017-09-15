import schedule
import time
import urllib
import pickle
import threading
from html import *
from sites import SITES_TO_VISIT

texts = {}



def get_htmls():

    for site in SITES_TO_VISIT:
        print "Getting html"
        
        url = site
        html = urllib.urlopen(url).read()
        text = (text_from_html(html))
        texts[site] = text
        pickle.dump( texts, open( "html_info.py", "wb" ) )


from screenshot import *


def make_screenshots():

    sites = [get_screen_shot(
        url= site, filename=SITES_TO_VISIT[site]['pic'], path='./static/img',
        crop=True, crop_replace=False,
        thumbnail=True, thumbnail_replace=False,
        thumbnail_width=500, thumbnail_height=600,
    ) for site in SITES_TO_VISIT.keys() ]


def run_jobs():
    gh = threading.Thread(name='get_htmls', target=get_htmls)
    ms = threading.Thread(name='make_screenshots', target=make_screenshots)
    gh.start()
    ms.start()


if __name__ == "__main__":
    schedule.every(1).minutes.do(run_jobs)

    while 1:
        schedule.run_pending()
        time.sleep(1)