#This is the main file for the vulnerability scanning API.
#You'll find that this file is very small. It's only job is to initialize the Flask server,
#and to respond to requests coming to the root URL (/)
from flask import Flask, render_template, request, Response
import json, requests, configparser


#We get the configuration.ini file to check where the API is located
config = configparser.ConfigParser()
config.read('configuration.ini')

#We get the api_url variable and print it for debugging purposes
global api_url
api_url = config['DEFAULT']['api_url']
print(api_url)

#We need this for the Flask server to run
app = Flask(__name__, template_folder='templates')

#Printing the route map for debugging purposes
print(app.url_map)

#Code executed when someone reached out to the / path
@app.route('/')
@app.route('/index')
def main():
    return render_template('index.html', ip=request.remote_addr)

#Calling the ping path on the API calls the /ping/ path on the API
@app.route('/ping/<target>')
def ping(target):
    print("Calling : " + api_url + "/ping/" + target)
    result = requests.get(api_url + "/ping/" + target)
    result = result.json()
    return render_template('ping.html', json=result, message_list=['Ping command done !'])


#Portscan
@app.route('/portscan/<target>')
def portscan(target):
    result = requests.get(api_url + "/portscan/" + target)
    result = result.json()
    return render_template('portscan.html', json=result, message_list=['Portscan done !'])


#Deep service scan
@app.route('/servicescan/<target>/<ports>')
def servicescan(target, ports):
    result = requests.get(api_url + "/servicescan/" + target + "/" + ports)
    result = result.json()
    return render_template('servicescan.html', json=result, message_list=['Service scan done !'])


#SSL ciphers list check
@app.route('/cipherscan/<target>')
def cipherscan(target):
    result = requests.get(api_url + "/cipherscan/" + target)
    result = result.json()
    return render_template('cipherscan.html', json=result, message_list=['Cipher scan done !'])

@app.route('/setapi/<url>')
def setapi(url):
    global api_url
    api_url = "http://" + url
    file = open("configuration.ini","w+") 
    file.write("[DEFAULT]\napi_url = " + api_url)
    file.close()
    return Response(url)

@app.route('/subdomains/<target>')
def subdomains(target):
    print("Calling : " + api_url + "/subdomains/" + target)
    result = requests.get(api_url + "/subdomains/" + target)
    result = result.json()
    return render_template('subscan.html', json=result, message_list=['Subdomain scan finished!'])

@app.route('/databasescan/<target>')
def databasescan(target):
    print("Calling : " + api_url + "/databasescan/" + target)
    result = requests.get(api_url + "/databasescan/" + target)
    result = result.json()
    return render_template('databasescan.html', json=result, message_list=['DB scan finished!'])