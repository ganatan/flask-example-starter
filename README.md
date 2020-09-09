# Flask Example Starter

# [Live Demo](#live-demo)
Here is a working live demo :  https://flask.ganatan.com


## Quick start

```bash
# clone the repo
git clone https://github.com/ganatan/flask-example-starter.git

# change directory
cd flask-example-starter

# Linux
export FLASK_APP=flaskr
export FLASK_ENV=development

# Windows Shell
$env:FLASK_APP = "flaskr"
$env:FLASK_ENV = "development"

# install the SQLite Database
Flask create-database

# Import Default Data
Flask import-database

# Method 1 : execute application on flask-example-starter/flaskr
flask run

# Method 2 : execute application on flask-example-starter
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

# Copy theses files the repo on tis directory
home/service/flask-frontend

# Change the config
etc/apache2/sites-available/000-default.conf


# Change proprietaire
sudo chown -hR www-data /home/services/flask-frontend

# Verifier droits ecritures sur le fichier
sudo chmod +rwx /home/services/flask-frontend/instance/flaskr.sqlite

flask create-database

flask import-database

sudo service apache2 restart

```


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

