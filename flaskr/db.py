import sqlite3

import click
from flask import current_app
from flask import g
from flask.cli import with_appcontext


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


def create_database():
    db = get_db()

    with current_app.open_resource("scripts/create.sql") as f:
        db.executescript(f.read().decode("utf8"))

def import_database():
    db = get_db()

    with current_app.open_resource("scripts/import.sql") as f:
        db.executescript(f.read().decode("utf8"))


@click.command("create-database")
@with_appcontext
def create_database_command():
    create_database()
    click.echo("Initialized the database.")

@click.command("import-database")
@with_appcontext
def import_database_command():
    import_database()
    click.echo("Import Default Data.")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(create_database_command)
    app.cli.add_command(import_database_command)
