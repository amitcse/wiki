import random
import string
import hashlib

def make_salt():
    return ''.join(random.choice(string.letters) for x in range(0,5))

def make_passwd_hash(name, pwd, salt=None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pwd + salt).hexdigest()
    return' %s|%s' % (h,salt)

def valid_pw(name, passwd, h):
    salt = h.split('|')[1]
    return h==make_passwd_hash(name, passwd, salt)
