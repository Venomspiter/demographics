from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)
  
def get_state_options():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    state = counties[0]["State"]
    pick = ""
    for c in counties:
        if state != c["State"]:
            pick += Markup("<option value=" + state +">" + state + "</option>")
            state = c["State"]
    return pick
        
def funfact(state):
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    fact = 0
    for c in counties:
        if state == c["State"]:
            fact += c["Miscellaneous"]["Percent Female"]
    return fact
        
@app.route("/")
def render_main():
    return render_template('home.html', option = get_state_options())
    
@app.route("/app", methods=['GET','POST'])
def get_fact():  
    area = request.args['pickstate']
    return render_template('index.html', fact = funfact(area), option = get_state_options())
        
if __name__=="__main__":
    app.run(debug=False, port=54321)
