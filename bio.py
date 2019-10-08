from flask import Flask, request, render_template, redirect    
import os,optparse 
import yaml

app = Flask(__name__)
app.static_folder = 'templates'
environment=os.getenv("ENVIRONMENT","development")
environment=os.getenv("ENVIRONMENT","development")
with open("links.yaml", 'r',encoding='utf-8') as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
 
@app.route("/")
def home():
    return render_template('index.html', data=data)  
    
if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    app.run(host="0.0.0.0",debug=debug) # run the flask app