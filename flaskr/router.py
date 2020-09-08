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
    items = [
        {'name': 'Alerts', 'link': 'alerts'},
        {'name': 'Badges', 'link': 'badges'},
        {'name': 'Buttons', 'link': 'buttons'},
        {'name': 'Blockquotes', 'link': 'blockquotes'},
        {'name': 'Breadcrumb', 'link': 'breadcrumb'},
        {'name': 'Collapse', 'link': 'collapse'},
        {'name': 'Dropdowns', 'link': 'dropdowns'},
        {'name': 'Forms', 'link': 'forms'},
        {'name': 'List-group', 'link': 'list-group'},
        {'name': 'Modal', 'link': 'modal'},
        {'name': 'Pagination', 'link': 'pagination'},
        {'name': 'Popovers', 'link': 'popovers'},
        {'name': 'Progress', 'link': 'progress'},
        {'name': 'Spinners', 'link': 'spinners'},
        {'name': 'Toasts', 'link': 'toasts'},
        {'name': 'Tooltips', 'link': 'tooltips'},
    ]
    return render_template('index.html',  application=application, items=items)


@ routes.route('/about')
def about():
    return render_template('pages/about.html')


@ routes.route('/contact')
def contact():
    return render_template('pages/contact.html')


@ routes.route('/<page>')
def show(page):
    try:
        return render_template('bootstrap/%s.html' % page)
    except TemplateNotFound:
        return render_template('pages/404.html')
