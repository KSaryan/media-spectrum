import schedule
import time
import urllib
import pickle
import threading
from html import *
from model import Site

texts = {}



def get_htmls():
    urls = db.session.query(Site.url).all()

    for url in urls:
        print "Getting html"
        
        html = urllib.urlopen(url).read()
        text = (text_from_html(html))
        texts[site] = text
        pickle.dump( texts, open( "html_info.py", "wb" ) )


from screenshot import *

def make_screenshots():
    print "Getting screenshot"
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

    schedule.every(5).minutes.do(run_jobs)

    while True:
        schedule.run_pending()
        time.sleep(1)
