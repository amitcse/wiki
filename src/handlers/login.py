from base import BaseHandler
from src.utilities.FormVerification import *
from src.utilities import UserDatastore
from src.utilities.Hashing import *
from src.utilities.ValidateCookies import *

class LoginHandler(BaseHandler):
    
    def get(self):
        self.render("login.html")
        
    def post(self):
        have_error = False
        error = "Invalid Login !!"
        username = self.request.get('username')
        passwd = self.request.get("password")
        
        if not valid_username(username) or not valid_password(passwd):
            have_error = True
        
        if not have_error:
            user = WikiUser.gql("WHERE username = :1",username).get()
            if user:
                hashval = user.hashval
                if valid_pw(username, passwd, hashval):
                    uid = user.key().id()
                    self.response.headers.add_header('Set-Cookie', 'u_id=%s; Path=/'%make_secure(str(uid)))
                    self.redirect("/")
                else:
                    have_error = True
            else:
                have_error = True
                
        if have_error:
            self.render("login.html", error = error)
            
