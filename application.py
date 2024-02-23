# application.py
from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello():
    return "<h1>Hello, this is a sample Flask web application and deploy by Code pipeline! on AWS</h1>"

if __name__ == '__main__':
    application.run()
