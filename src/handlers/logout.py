from base import BaseHandler

class LogoutHandler(BaseHandler):
    def get(self):
        self.response.headers.add_header('Set-Cookie', 'u_id=%s; Path=/'%"")