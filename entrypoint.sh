#!/bin/sh

cd /app
pip3 install -r requirements.txt
pip3 install --upgrade pip

gunicorn -c gunicorn_conf.py rich:app -b 0.0.0.0:8800