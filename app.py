#This is the main file for the vulnerability scanning API.
#You'll find that this file is very small. It's only job is to initialize the Flask server,
#and to respond to requests coming to the root URL (/)
from flask import Flask, render_template, request

#We need this for the Flask server to run
app = Flask(__name__, template_folder='templates')

#Printing the route map for debugging purposes
print(app.url_map)

#Code executed when someone reached out to the / path
@app.route('/')
@app.route('/index')
def main():
    return render_template('index.html', ip=request.remote_addr)