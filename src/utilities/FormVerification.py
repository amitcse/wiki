import re
import cgi
from google.appengine.ext import db
from UserDatastore import WikiUser

USER_RE = re.compile("^[a-zA-Z0-9_-]{3,20}$")
USERP_RE = re.compile("^.{3,20}$")
USERMAIL_RE = re.compile("^[\S]+@[\S]+\.[\S]+$")

def escape_html(s):
    return cgi.escape(s, quote = True)

def valid_username(username):
    return username and USER_RE.match(username)

def valid_password(password):
    return password and USERP_RE.match(password)

def verify_password(new, old):
    return new==old

def valid_email(email):
    return not email or USERMAIL_RE.match(email)

def validate_user(username):
    result = db.Query(WikiUser).filter("username =", username).fetch(limit=1)
    return result
