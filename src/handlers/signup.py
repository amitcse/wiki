from base import BaseHandler
from src.utilities.FormVerification import *
from src.utilities.UserDatastore import *
from src.utilities.Hashing import *
from src.utilities.ValidateCookies import *


class SignupHandler(BaseHandler):
    
    def get(self):
        self.render("signup.html")
        
    def post(self):
        
        have_error = False
        user_name = self.request.get('username')
        user_passwd = self.request.get('password')
        user_verify = self.request.get('verify')
        user_email = self.request.get('email')
        
        
        params = dict(username = user_name,
                      email = user_email)
        
        if not valid_username(user_name):
            params['error_username'] = "That's not a valid username."
            have_error = True
        else:
            res = validate_user(user_name)
            if res:
                params['error_username'] = "User already exists."
                have_error = True
                
        if not valid_password(user_passwd):
            params['error_password'] = "That wasn't a valid password"
            have_error = True
        elif user_passwd!=user_verify:
            params['error_verify'] = "Your passwords didn't match."
            have_error = True
        
        if not valid_email(user_email):
            params['error_email'] = "That's not a valid email."
            have_error = True
            
        if have_error:
            self.render("signup.html", **params)
            
        else:
            if user_email:
                user = WikiUser(username = user_name, hashval = make_passwd_hash(user_name, str(user_passwd)), email = user_email)
            else:
                user = WikiUser(username = user_name, hashval = make_passwd_hash(user_name, str(user_passwd)))
            
            user.put()
            uid = user.key().id()
            self.response.headers.add_header('Set-Cookie','u_id=%s; Path=/'%make_secure(str(uid)))
            
            self.redirect('/')