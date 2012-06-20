import webapp2
from src.handlers.signup import *
from src.handlers.login import *
from src.handlers.logout import *
from src.handlers.wiki import *


app = webapp2.WSGIApplication([('/signup',SignupHandler),
                              ('/login',LoginHandler),('/logout', LogoutHandler),
                              ('/_edit(/?(?:[a-zA-Z0-9_-]+/?)*)',EditPageHandler),
                              ('/_history(/?(?:[a-zA-Z0-9_-]+/?)*)', HistoryHandler),
                              ('(/?(?:[a-zA-Z0-9_-]+/?)*)',WikiPageHandler)],
                              debug = True)