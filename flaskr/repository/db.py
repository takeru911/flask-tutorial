import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext


def init(app):
    _init_app(app)


def _init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def _init_db():
    db = _get_db()
    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf-8"))


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    _init_db()
    click.echo("Initialized the database.")


def _get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def query(sql: str, values: tuple = ()):
    db = _get_db()
    result = db.execute(sql, values).fetchall()
    db.commit()
    return result


def close_db(*args):
    db = g.pop("db", None)
    if db is not None:
        db.close()
