FROM ubuntu:20.04

ENV LANG C.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL C.UTF-8  

ARG DEBIAN_FRONTEND=noninteractive

COPY . /root/yavs-gui
RUN cd /root/yavs-gui

RUN /root/yavs-gui/install.sh
WORKDIR /root/yavs-gui

ENV FLASK_APP app.py

EXPOSE 8001
CMD ["/bin/bash", "-c", "gunicorn --bind=0.0.0.0:8001 app:app"]
