import webapp2
import cgi
from google.appengine.api import users
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

MAIN_PAGE_HTML = """\
<!doctype html>
<html>
    <body>
        <h1>Jersey Size Calculator</h1>
        <p></p>
        <form method="post">
            <label for="Feet"> Height (in feet):</label>
            <input name="Feet" type = "number" min= "0">
            <label for="Inches"> inches:</label>
            <input name="Inches" type = "number" min= "0" max ="11">
            <br>
            
            <label for="Weight"> Weight (in pounds):</label>
            <input name="Weight" type = "number" min="0"><br>
            <input name="" type="submit" value ="submit">
    </body>
</html>"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
    def post(self):
        weight = self.request.get("Weight")
        inches = self.request.get("Inches")
        feet = self.request.get("Feet")
        height = int(feet * 12) + int(inches)
        score = int(weight) + height 
        size = ""
        if score < 200 and weight < 150:
            size ="Search for Youth Jerseys"
        elif score < 200:
            size = "Small"
        elif score < 300:
            size = "Medium"
        elif score < 400:
            size = "Large"
        elif score > 400:
            size = "Search for jerseys under extra large or above"
        self.response.write(size)
        

    
application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

