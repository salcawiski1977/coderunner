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

class python(ndb.Model):

    question = ndb.StringProperty(required=True)
    right_answer = ndb.StringProperty(required=True)
    wrong_answer1 = ndb.StringProperty(required=True)
    wrong_answer2 = ndb.StringProperty(required=True)

class javascript(ndb.Model):

    question = ndb.StringProperty(required=True)
    right_answer = ndb.StringProperty(required=True)
    wrong_answer1 = ndb.StringProperty(required=True)
    wrong_answer2 = ndb.StringProperty(required=True)
    
class html(ndb.Model):

    question = ndb.StringProperty(required=True)
    right_answer = ndb.StringProperty(required=True)
    wrong_answer1 = ndb.StringProperty(required=True)
    wrong_answer2 = ndb.StringProperty(required=True)

def get_python_questions():
#    newQuestion = python(question="test", right_answer="test", wrong_answer1 = "test", wrong_answer2 = "test")
#    newQuestion.put()
    questions = python.query().fetch()
    return questions

def get_html_questions():
#    newQuestion = python(question="test", right_answer="test", wrong_answer1 = "test", wrong_answer2 = "test")
#    newQuestion.put()
    questions = html.query().fetch()
    return questions

def get_javascript_questions():
#    newQuestion = python(question="test", right_answer="test", wrong_answer1 = "test", wrong_answer2 = "test")
#    newQuestion.put()
    questions = html.query().fetch()
    return questions

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template('template/menuscreen.html')
        self.response.write(results_template.render())
        
class JavascriptHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template('template/JavaScript.html')
        questions = get_javascript_questions()
        the_variable_dict = {
            "questionA": questions[0].question,
            "answerA1": questions[0].right_answer,
            "answerA2": questions[0].wrong_answer1,
            "answerA3": questions[0].wrong_answer2,
            "questionB": questions[1].question,
            "answerB1": questions[1].wrong_answer1,
            "answerB2": questions[1].right_answer,
            "answerB3": questions[1].wrong_answer2,
            "questionC": questions[2].question,
            "answerC1": questions[2].wrong_answer2,
            "answerC2": questions[2].wrong_answer1,
            "answerC3": questions[2].right_answer,
        }
    
        self.response.write(results_template.render(the_variable_dict))
      
        
class PythonHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template('template/Python.html')
        questions = get_python_questions()
        the_variable_dict = {
            "questionA": questions[0].question,
            "answerA1": questions[0].right_answer,
            "answerA2": questions[0].wrong_answer1,
            "answerA3": questions[0].wrong_answer2,
            "questionB": questions[1].question,
            "answerB1": questions[1].wrong_answer1,
            "answerB2": questions[1].right_answer,
            "answerB3": questions[1].wrong_answer2,
            "questionC": questions[2].question,
            "answerC1": questions[2].wrong_answer2,
            "answerC2": questions[2].wrong_answer1,
            "answerC3": questions[2].right_answer,
        }
        self.response.write(results_template.render(the_variable_dict))
        
class HtmlHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template('template/HTML.html')
        questions = get_html_questions()
        the_variable_dict = {
            "questionA": questions[0].question,
            "answerA1": questions[0].right_answer,
            "answerA2": questions[0].wrong_answer1,
            "answerA3": questions[0].wrong_answer2,
            "questionB": questions[1].question,
            "answerB1": questions[1].wrong_answer1,
            "answerB2": questions[1].right_answer,
            "answerB3": questions[1].wrong_answer2,
            "questionC": questions[2].question,
            "answerC1": questions[2].wrong_answer2,
            "answerC2": questions[2].wrong_answer1,
            "answerC3": questions[2].right_answer,
        }
        self.response.write(results_template.render(the_variable_dict))
        
class CreditsHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template('template/menuscreen.html')
        self.response.write(results_template.render())   
        
# Route mapping
app = webapp2.WSGIApplication([
    # This line routes the main url ('/')  - also know as
    # The root route - to the Fortune Handler
    ('/', HomeHandler),
    ('/JavaScript', JavascriptHandler),
    ('/Credits', CreditsHandler),
    ('/Python', PythonHandler),
    ('/HTML',HtmlHandler)
], debug=True)