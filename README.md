# Flask Example Starter

# [Live Demo](#live-demo)
Here is a working live demo :  https://flask.ganatan.com


## Quick start

```bash
# clone the repo
git clone https://github.com/ganatan/flask-example-starter.git

# change directory
cd flask-example-starter

# On Linux
export FLASK_APP=flaskr
export FLASK_ENV=development

# On Windows Shell
$env:FLASK_APP = "flaskr"
$env:FLASK_ENV = "development"

# install the SQLite Database
Flask create-database

# Import Default Data
Flask import-database

# Method 1 : Factory with flask-example-starter/flaskr/__init__.py
flask run

# Method 2 : Application with flask-example-starter/app.py
py app.py

```
in your browser go to [http://localhost:5000](http://localhost:5000) 

## Deploy on Linux Apache

```bash

# Update Ubuntu/Debian
sudo apt-get update && sudo apt-get upgrade -yes

# Install apache
sudo apt install apache2 -y

# Verify Python
python3 --version

# Install Python
sudo apt-get install python3.8 --yes !!! if not installed

# Verify Python pip
pip3 --version

# Install Python pip
sudo apt-get install python3-pip --yes

# Verify Flask
flask --version

# Install Flask
sudo pip3 install flask

# Install wsgi
sudo apt-get install libapache2-mod-wsgi-py3 python-dev -y

# Activate wsgi
sudo a2enmod wsgi

# Copy all files the repo on this directory
home/service/flask-frontend

# Copy the apache config on
etc/apache2/sites-available/000-default.conf

# Change persmission on Database SQLite3 File
sudo chown -hR www-data /home/services/flask-frontend

# Verifier droits ecritures sur le fichier
sudo chmod +rwx /home/services/flask-frontend/instance/flaskr.sqlite

# Create Database
flask create-database

# Import Data on Database
flask import-database

# Restart Apache
sudo service apache2 restart

```

in your browser go to [http://your-ip-address](http://your-ip-address) 


### Author
* Updated : 09/09/2020
* Author  : danny

### Documentation

English Tutorials
- Installation - https://www.ganatan.com/tutorials/en

Tutoriels en français
- Installation - https://www.ganatan.com/tutorials/

- Tutoriel Python - https://www.ganatan.com/tutorials/python-avec-angular
- Tutoriel Django - https://www.ganatan.com/tutorials/django-avec-angular
- Tutoriel Flask - https://www.ganatan.com/tutorials/flask-avec-angular

