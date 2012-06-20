import hmac
import SecretData
from google.appengine.ext import db

def hash_str(s):
    return hmac.new(SecretData.SECRET,s).hexdigest()

def make_secure(s):
    return "%s|%s" % (s,hash_str(s))

def check_secure(h):
    split_val = h.split('|')
    if len(split_val)!=2:
        return None
    val = split_val[0]
    if h == make_secure(val):
        return val

def validate_user_cookie(cookie_str):
    if not cookie_str:
        return None
    cookie_val = check_secure(cookie_str)

    if cookie_val:
        uid = int(cookie_val)
        ky = db.Key.from_path('WikiUser',uid)
        user = db.get(ky)
        if user:
            return user.username
        else:
            return None
    else:
        return None

