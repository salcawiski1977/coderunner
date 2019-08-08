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

def get_all_questions():
    #fillings = ['steak', 'carnitas', 'veggie', 'chicken', 'ground beef']
    Questions = python.query().filter().fetch()
    only_Questions = []
    for Question in Questions:
        only_Questions.append((Question.right_answer))
    return only_Questions

def get_python_questions():
    #fillings = ['steak', 'carnitas', 'veggie', 'chicken', 'ground beef']
#    newQuestion = python(question="test", right_answer="test", wrong_answer1 = "test", wrong_answer2 = "test")
#    newQuestion.put()
    questions = python.query().fetch()
    return questions

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template('template/menuscreen.html')
        self.response.write(results_template.render())
        
class JavascriptHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template('template/JavaScript.html')
        self.response.write(results_template.render(questionsC = get_all_questions()))

        
class CreditsHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template('template/menuscreen.html')
        self.response.write(results_template.render())        
        
class QuestionsHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template('template/Python.html')
        questions = get_python_questions()
        the_variable_dict = {
            "question": questions[0].question,
            "answer1": questions[0].right_answer,
            "answer2": questions[0].wrong_answer1,
            "answer3": questions[0].wrong_answer2
        }
        self.response.write(results_template.render(the_variable_dict))
        
#        self.response.write(get_all_questions())
        
# Route mapping
app = webapp2.WSGIApplication([
    # This line routes the main url ('/')  - also know as
    # The root route - to the Fortune Handler
    ('/', HomeHandler),
    ('/Javascript', JavascriptHandler),
    ('/Credits', CreditsHandler),
    ('/Python', QuestionsHandler),
], debug=True)