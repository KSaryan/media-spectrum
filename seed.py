# from sqlalchemy import func
from model import (User, Site, FaveSite)
from flask import Flask
from model import connect_to_db, db
import pickle


SITES_TO_VISIT = {
                  'https://www.nytimes.com': {'pic': 'nytimes.png', 'name': 'New York Times', 'route_name': 'NYT'},
                  'https://www.foxnews.com': {'pic': 'foxnews.png', 'name': 'Fox News', 'route_name': 'FoxNews'}, 
                  'https://www.motherjones.com': {'pic': 'motherjones.png', 'name': 'Mother Jones', 'route_name': 'MotherJones'}, 
                  'http://www.buzzfeednews.com': {'pic': 'buzzfeednews.png', 'name': 'BuzzFeed News', 'route_name': 'BuzzFeed'}, 
                  'http://www.washingtonpost.com': {'pic': 'washingtonpost.png', 'name': 'Washington Post', 'route_name': 'WashingtonPost'}, 
                  'https://www.reuters.com': {'pic': 'reuters.png', 'name': 'Reuters', 'route_name': 'Reuters'}, 
                  'https://www.axios.com': {'pic': 'axios.png', 'name': 'Axios', 'route_name': 'Axios'}, 
                  'http://www.politico.com': {'pic': 'politico.png', 'name': 'Politico', 'route_name': 'Politico'}, 
                  'https://www.wsj.com': {'pic': 'wsj.png', 'name': 'The Wall Street Journal', 'route_name': 'WSJ'}, 
                  'http://www.washingtontimes.com': {'pic': 'washingtontimes.png', 'name': 'The Washington Times', 'route_name': 'WashingtonTimes'},
                  'https://www.nypost.com': {'pic': 'nypost.png', 'name': 'New York Post', 'route_name': 'NYP'},
                  'http://www.nationalreview.com': {'pic': 'nationalreview.png', 'name': 'The National Review', 'route_name': 'NationalReview'},
                  'https://www.infowars.com': {'pic': 'infowars.png', 'name': 'Info Wars', 'route_name': 'InfoWars'},
                  'http://www.breitbart.com': {'pic': 'breitbart.png', 'name': 'Breitbart', 'route_name': 'Breitbart'},
                  'https://www.theguardian.com/us': {'pic': 'guardian.png', 'name': 'The Guardian', 'route_name': 'Guardian'},
                  'http://www.aljazeera.com/': {'pic': 'aljazeera.png', 'name': 'Al Jazeera', 'route_name': 'AlJazeera'},
                  'https://www.npr.org/': {'pic': 'npr.png', 'name': 'NPR', 'route_name': 'NPR'},
                  'http://www.drudgereport.com/': {'pic': 'drudge.png', 'name': 'Drudge Report', 'route_name': 'DrudgeReport'},
                  'http://www.washingtonexaminer.com/': {'pic': 'washingtonexaminer.png', 'name': 'Washington Examiner', 'route_name': 'WashingtonExaminer'},
                  'https://www.vox.com/': {'pic': 'vox.png', 'name': 'Vox', 'route_name': 'Vox'},
                  'https://www.csmonitor.com/': {'pic': 'csmonitor.png', 'name': 'Christian Science Monitor', 'route_name': 'CSMonitor'}
                  }

def load_sites():
    for site in SITES_TO_VISIT:
        site_name = SITES_TO_VISIT[site]['name']
        route_name = SITES_TO_VISIT[site]['route_name']
        pic_name = SITES_TO_VISIT[site]['pic']
        url = site
        new_site = Site(site_name=site_name, route_name=route_name, pic_name=pic_name, url=url)
        db.session.add(new_site)
        db.session.commit()


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    db.create_all()
    load_sites()

    


