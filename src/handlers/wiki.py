from base import BaseHandler
from src.utilities.ValidateCookies import *
from src.utilities.PostDatastore import *
import logging


class WikiPageHandler(BaseHandler):
    
    def get(self, resource):
        #logging.error("main_page"+resource)
        if resource=="":
            resource = '/'
        logged_in = False
        username = validate_user_cookie(self.request.cookies.get('u_id'))
        if username:
            logged_in = True
        pid = self.request.get('pid')
        if pid:
            post = WikiPost.get_by_id(int(pid))
        else:
            q = db.GqlQuery("SELECT * FROM WikiPost where posttitle = :1 ORDER BY created DESC LIMIT 1", resource)
            post = q.get()
        if post:
            self.render("wikifront.html", logged_in = logged_in, username = username, post = post)
        else:
            if logged_in:
                resource = resource.rstrip('/').split('/')[-1]
                self.redirect('/_edit/%s' % resource)
            else:
                self.redirect('/login')
        
        
        
        
class EditPageHandler(BaseHandler):
    
    def get(self, resource):
        #logging.info("edit_page"+resource)
        if resource=="":
            resource = '/'
        logged_in = False
        username = validate_user_cookie(self.request.cookies.get('u_id'))
        if username:
            logged_in = True
            pid = self.request.get('pid')
            if pid:
                post = WikiPost.get_by_id(int(pid))
            else:
                q = db.GqlQuery("SELECT * FROM WikiPost where posttitle = :1 ORDER BY created DESC LIMIT 1", resource)
                post = q.get()
            if post:
                content = post.content
            else:
                content = ""
            self.render("wikinewpost.html", logged_in = logged_in, username = username, content = content)
            
            
        else:
            self.redirect('/login')
        
    def post(self, resource):
        logging.info('post_resource'+resource)
        if resource == '/':
            posttitle = resource
            redirect_link = ""
        else:
            #url = self.request.url
            redirect_link = resource.rstrip('/').split('/')[-1]
            posttitle = '/' + redirect_link
        #logging.error('posttitle_'+posttitle)
        content = self.request.get('content')
        post = WikiPost(posttitle = posttitle, content = content)
        post.put()
        self.redirect('/%s' % redirect_link)
        
    
class HistoryHandler(BaseHandler):
    
    def get(self, resource):
        logging.info('history'+resource)
        if resource=="":
            resource = '/'
        logged_in = False
        
        username = validate_user_cookie(self.request.cookies.get('u_id'))
        if username:
            logged_in = True
        posts = db.GqlQuery("Select * from WikiPost where posttitle = :1 order by created desc ", resource)
        if logged_in:
            posts = list(posts)
            if posts:
                self.render("wikiposthistory.html",logged_in = logged_in, username = username, posts = posts)
            else:
                resource = resource.rstrip('/').split('/')[-1]
                self.redirect('/_edit/%s' % resource)
        else:
            self.redirect('/login')