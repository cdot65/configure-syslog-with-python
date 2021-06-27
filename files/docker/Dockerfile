FROM python:slim-buster

### -------------------------------------------------
### Metadata information
### -------------------------------------------------
LABEL name="juniper-automation-container"
LABEL maintainer="cremsburg@protonmail.com"
LABEL description="ansible container to manage Juniper devices"
LABEL license="GPLv3"
LABEL url="https://gitlab.com/cremsburg/juniper-automation-container/container_registry"
LABEL build-date="20210627"

### -------------------------------------------------
### Change directory to /var/tmp/
### -------------------------------------------------
WORKDIR /var/tmp/

### -------------------------------------------------
### Add and install python packages
### -------------------------------------------------
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install --upgrade pip

### -------------------------------------------------
### Copy JSNAPy goodies
### -------------------------------------------------
COPY jsnapy.cfg /etc/jsnapy/jsnapy.cfg
RUN mkdir /etc/jsnapy/snapshots
RUN mkdir /etc/jsnapy/tests
