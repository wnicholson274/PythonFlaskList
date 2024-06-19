# imports flask from the flask module
from flask import Flask 

# creates an instance of the flask class
app = Flask(__name__)

# defines a route for the URL 

#@app.route("/") This is a # so it does not make errors without python code. please remove 

# runs the flask web server
app.run(host='0.0.0.0', port=5000)