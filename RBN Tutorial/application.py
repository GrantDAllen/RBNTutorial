from flask import Flask

#@application.route("/")
#def index():
#    return "Index Page"

def hello_word():
    return "Hello, World!"
    

application = Flask(__name__)

application.add_url_rule('/')

application.run()