# application.py
from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello():
    return "<h1>Hello, this is a simple Flask web application and deply by Code pipeline!</h1>"

if __name__ == '__main__':
    application.run()
