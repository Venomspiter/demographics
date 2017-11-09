from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    color = request.args[ 'color' ]
    #The request object stores info about the request sent to the server
    #args is a multiplicit (like a dictionary but can have multiple values for the same key)
    #The info in args is visible in the url for the page being requested (ex. .../response)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
