from google.appengine.ext import db

class WikiPost(db.Model):
    posttitle = db.StringProperty()
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    