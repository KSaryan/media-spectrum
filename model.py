from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """Users table"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)


    def __repr__ (self):
        """Displayed when called"""

        return "<%s: %s>" %(self.user_id, self.user_name)

class Site(db.Model):
    """Websites to scrape and screen capture"""

    __tablename__= "sites"

    site_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    site_name = db.Column(db.String(25), nullable=False)
    route_name = db.Column(db.String(25), nullable=False)
    pic_name = db.Column(db.String(25), nullable=False)
    url = db.Column(db.String(75), nullable=False)
    html = db.Column(db.Text)

    def __repr__(self):
        """Displayed when called"""

        return "<%s>" %(self.site_name)

class FaveSite(db.Model):
    """Users favorites sites"""

    __tablename__ = "faves"

    fs_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    site_id = db.Column(db.Integer, db.ForeignKey('sites.site_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    user = db.relationship('User', backref='faves')
    site = db.relationship('Site', backref='faves')

    def __repr__(self):
        """Displayed when called"""

        return "<fs_id:%s, site: %s, user: %s>" %(self.fs_id, self.site.site_name, self.user.user_name)


def connect_to_db(app, db_uri = "postgres:///medias"):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    app = Flask(__name__)
    connect_to_db(app)
    db.create_all()
    print "Connected to DB."