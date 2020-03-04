# yavs-gui

This project will allow you to deploy a web interface for our other project, [YAVS](https://github.com/Couaque/yavs).

## Installation
```
git clone https://github.com/Couaque/yavs-gui
cd yavs-gui
sudo ./install.sh
```
## Configuration
It is required that you modify the content of **configuration.ini** so that it contains where your API endpoint is. If you don't do it you won't be able to retrieve any information from the API. Please add a line inside as follows :
```
[DEFAULT]
api_url = http://<API_FQDN>:<port>
```
And because this project is available on the network and runs only on Linux, here is a pro tip : you can't bind ports < 1024 if you are not root.

## Run the GUI
### For testing purposes
To run this GUI for testing purposes or from your own laptop / raspberry, you can use the following command once you're in the yavs-gui main directory :
```
flask run -p <port>
```
This will allow you to run the GUI from localhost with the port that you chose. Please double check the API to be sure that this is working as intended.

## Dependancies
- Python 2 & 3
- Flask
- Jinja 2