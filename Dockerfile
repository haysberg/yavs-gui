FROM ubuntu:20.04

ENV LANG C.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL C.UTF-8  

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && apt full-upgrade -y
RUN apt install -y python3-pip
RUN apt install -y python3-flask libcairo2 libglib2.0-0
RUN apt install -y build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
RUN pip3 install flask xmltodict ujson requests gunicorn


COPY . /root/yavs-gui
RUN cd /root/yavs-gui

RUN /root/yavs-gui/install.sh
WORKDIR /root/yavs-gui

ENV FLASK_APP app.py

EXPOSE 8001
CMD ["/bin/bash", "-c", "gunicorn --bind=0.0.0.0:8001 app:app"]
