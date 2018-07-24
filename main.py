import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_vars = {
            'name_of_game': self.request.get('game')
        }
        main_template = JINJA_ENVIRONMENT.get_template('templates/main.html')
        self.response.write(main_template.render(template_vars))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
