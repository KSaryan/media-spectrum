import schedule
from screenshot import *
import time



SITES_TO_VISIT = {'nytimes.com': 'nytimes.png', 'foxnews.com': 'foxnews.png'}


def make_screenshots():

	sites = [get_screen_shot(
        url='https://www.' + site, filename=SITES_TO_VISIT[site], path='./static/img',
        crop=True, crop_replace=False,
        thumbnail=True, thumbnail_replace=False,
        thumbnail_width=500, thumbnail_height=600,
    ) for site in SITES_TO_VISIT.keys() ]


schedule.every(1).minutes.do(make_screenshots)

while 1:
    schedule.run_pending()
    time.sleep(1)
