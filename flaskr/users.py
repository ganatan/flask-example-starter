from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint("users", __name__)

@bp.route("/users")
def users():
    db = get_db()
    items = db.execute(
        "SELECT id, username"
        " FROM user"
        " ORDER BY id ASC"
    ).fetchall()
    return render_template("users/items.html", items=items)
    

