#This is the main file for the vulnerability scanning API.
#You'll find that this file is very small. It's only job is to initialize the Flask server,
#and to respond to requests coming to the root URL (/)
from flask import Flask, render_template, request, Response, url_for
import json, requests, configparser, weasyprint, string, random, os
from flask_weasyprint import HTML, render_pdf

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
    return render_template('ping.html', ping_json=result, message_list=['Ping command done !'])


#Portscan
@app.route('/portscan/<target>')
def portscan(target):
    result = requests.get(api_url + "/portscan/" + target)
    result = result.json()
    return render_template('portscan.html', portscan_json=result, message_list=['Portscan done !'])


#Deep service scan
@app.route('/servicescan/<target>/<ports>')
def servicescan(target, ports):
    result = requests.get(api_url + "/servicescan/" + target + "/" + ports)
    result = result.json()
    return render_template('servicescan.html', service_json=result, message_list=['Service scan done !'])


#SSL ciphers list check
@app.route('/cipherscan/<target>')
def cipherscan(target):
    result = requests.get(api_url + "/cipherscan/" + target)
    result = result.json()
    return render_template('cipherscan.html', cipher_json=result, message_list=['Cipher scan done !'])

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
    return render_template('subscan.html', sub_json=result, message_list=['Subdomain scan finished!'])

@app.route('/databasescan/<target>')
def databasescan(target):
    print("Calling : " + api_url + "/databasescan/" + target)
    result = requests.get(api_url + "/databasescan/" + target)
    result = result.json()
    return render_template('databasescan.html', dbscan_json=result, message_list=['DB scan finished!'])
    
@app.route('/webappscan/<target>')
def webappscan(target):
    print("Calling : " + api_url + "/webappscan/" + target)
    result = requests.get(api_url + "/webappscan/" + target)
    result = result.json()
    return render_template('webscan.html', webapp_json=result, message_list=['Webapp scan finished!'])

@app.route('/pdf/<path>')
def dlpdf(path):
    filepath = os.path.join(app.root_path, 'static', 'customlogos', path + '.pdf')
    f=open(filepath, "r", encoding = 'ISO-8859-1')
    pdf = f.read()
    print(pdf)
    return Response(pdf, mimetype="application/pdf")

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

@app.route('/fullscan/<target>')
@app.route('/fullscan/<target>/<dowebscan>/<render_as_pdf>')
def fullscan(target, dowebscan = "do", render_as_pdf = True):
    print("Calling : " + api_url + "/fullscan/" + target)

    ping = requests.get(api_url + "/ping/" + target)
    ping = ping.json()

    #We get the ports from the API
    ports = requests.get(api_url + "/portscan/" + target)
    ports = ports.json()

    if "443" in ports :
        ciphers = requests.get(api_url + "/cipherscan/" + target)
        ciphers = ciphers.json()
    else :
        ciphers = []
    
    portlist = []
    for key in ports :
        print(key)
        portlist.append(key)
        
    portstring = portlist[0]
    for port in portlist[1:] :
        portstring = portstring + ","
        portstring = portstring + port
    services = requests.get(api_url + "/servicescan/" + target + "/" + portstring)
    services = services.json()

    if dowebscan == "do" :
        nikto = requests.get(api_url + "/webappscan/" + target)
        nikto = nikto.json()
    else :
        nikto = []

    bytestring = render_template('fullscan.html', portscan_json=ports, cipher_json=ciphers, service_json=services, ping_json=ping, webapp_json=nikto)

    if render_as_pdf == "do" :
        return render_pdf(HTML(string=bytestring))

    return render_template('fullscan.html', portscan_json=ports, cipher_json=ciphers, service_json=services, ping_json=ping, webapp_json=nikto)