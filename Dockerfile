FROM ubuntu:20.04

ENV LANG C.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL C.UTF-8  

RUN apt update && apt full-upgrade -y
RUN apt install -y python3-pip
RUN apt install -y python3-flask
RUN pip3 install flask xmltodict ujson requests gunicorn


COPY . /root/yavs-gui
RUN cd /root/yavs-gui

RUN /root/yavs-gui/install.sh
WORKDIR /root/yavs-gui

ENV FLASK_APP app.py

EXPOSE 8001
CMD ["/bin/bash", "-c", "gunicorn --bind=0.0.0.0:8001 app:app"]
