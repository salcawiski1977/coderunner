import webapp2
import os
import random
import jinja2
#import taco_model

from google.appengine.ext import ndb

# Remember, you can get this by searching for jinja2 google app engine
jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template('template/CodeRunners.html')
        self.response.write(results_template.render())
        
class GamesHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template('template/CodeRunnerGame.html')
        self.response.write(results_template.render())
        
class CreditsHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template('template/Credits.html')
        self.response.write(results_template.render())
        
# Route mapping
app = webapp2.WSGIApplication([
    # This line routes the main url ('/')  - also know as
    # The root route - to the Fortune Handler
    ('/', HomeHandler),
    ('/Games', GamesHandler),
    ('/Credits', CreditsHandler),
], debug=True)