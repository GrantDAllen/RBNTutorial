from flask import Flask
application = Flask(__name__)
@application.route("/")


#def index():
#    return "Index Page"

def hello_word():
    return "Hello, World!"