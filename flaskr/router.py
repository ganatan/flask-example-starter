from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

routes = Blueprint('index', __name__)


@routes.route('/')
def index():
    application = {
        'name': 'flask-starter',
        'flask': 'Flask 1.1.2',
        'bootstrap': 'Bootstrap 4.5.2',
        'fontawesome': 'Font Awesome 5.14.0'
    }
    return render_template('index.html',  application=application)


@routes.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        return render_template('pages/404.html')
