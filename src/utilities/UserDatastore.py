from google.appengine.ext import db

class WikiUser(db.Model):
    username = db.StringProperty(required = True)
    hashval = db.StringProperty(required = True)
    email = db.EmailProperty()
    created = db.DateTimeProperty(auto_now_add = True)
    