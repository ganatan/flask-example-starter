# Flask Example Starter

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

# execute application
flask run

```
in your browser go to [http://localhost:5000](http://localhost:5000) 

# Deploy on Linux Apache
sudo apt-get update && sudo apt-get upgrade -yes
sudo apt install apache2 -y

sudo apt-get install python3.8 --yes
sudo apt-get install python3-pip --yes
sudo pip3 install flask         

# Verify 
python3 --version
pip3 --version
flask --version

sudo apt-get install libapache2-mod-wsgi-py3 python-dev -y

sudo a2enmod wsgi           !!!!!!!!!!! a faire si pas installe !!!!!!!!!!!!!!! 

# Repertoire 
home/service/flask-frontend
etc/apache2/sites-available/000-default.conf

sudo service apache2 restart

# Verifier droits ecritures sur le fichier
sudo chmod +rwx /home/services/flask-frontend/instance/flaskr.sqlite



### Author
* Updated : 08/09/2020
* Author  : danny

### Documentation

English Tutorials
- Installation - https://www.ganatan.com/tutorials/en

Tutoriels en français
- Installation - https://www.ganatan.com/tutorials/

- Tutoriel Python - https://www.ganatan.com/tutorials/python-avec-angular
- Tutoriel Django - https://www.ganatan.com/tutorials/django-avec-angular
- Tutoriel Flask - https://www.ganatan.com/tutorials/flask-avec-angular

