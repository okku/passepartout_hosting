#!/usr/bin/env python

import webapp2
import json
from google.appengine.api import urlfetch
import logging

api_url = "https://heynow2.appspot.com/v1/code/"

class MainHandler(webapp2.RequestHandler):
    def webcode(self, webcode):
        if len(webcode) == 5:
            url = api_url + webcode + "/"
            logging.info(url)
            # info = requests.get(url, verify = False).json()
            resp = urlfetch.fetch(url, validate_certificate=False)
            logging.info(resp.content)
            info = json.loads(resp.content)
            if "fbName" in info and "code" in info:
                redir = 'https://m.me/' + info.get("fbName").encode('ascii','ignore') + '?ref=lc1' + info.get("code").encode('ascii','ignore')
                logging.info(redir)
                return self.redirect(redir)
        return self.redirect('/')

app = webapp2.WSGIApplication([
     webapp2.Route(r'/<webcode:\w+>', handler=MainHandler, handler_method='webcode'),
], debug=False)
