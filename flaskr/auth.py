import functools

from flask import (
  Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.repository import user_repository

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        elif len(user_repository.find_user_by_name(username)) != 0:
            error = f"User {username} is already registered."

        if error is None:
            user_repository.register_user(username, password)
            return redirect(url_for("auth.login"))
        flash(error)
    return render_template("auth/register.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        check_password_result = user_repository.check_match_password(username, password)

        if check_password_result is None:
            error = "Incorrect username or password"
            flash(error)
            return render_template("auth/login.html")

        session.clear()
        session["user_id"] = check_password_result.id
        return redirect(url_for("index"))
    return render_template("auth/login.html")


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None
    else:
        g.user = user_repository.find_user_by_id(user_id)[0]


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)
    return wrapped_view
