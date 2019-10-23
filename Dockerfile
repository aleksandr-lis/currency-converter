FROM python:3
RUN apt-get update
RUN apt-get install -y cron

COPY app/requirements.txt ./
RUN pip3 install -r requirements.txt
