from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.model import UserBlog
from flaskr.repository import blog_repository, user_blog_repository

bp = Blueprint("blog", __name__)


@bp.route("/")
def index():
    posts = user_blog_repository.fetch_all()

    return render_template("blog/index.html", posts=posts)


@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]

        if not title:
            error = "Title is required"
            flash(error)
            return render_template("blog/create.html")

        blog_repository.post_blog(title, body, g.user.id)
        return redirect(url_for("blog.index"))

    return render_template("blog/create.html")


def get_post(blog_id: int, check_author=True) -> UserBlog:
    posts = user_blog_repository.find_user_blog_by_blog_id(blog_id)

    if len(posts) == 0:
        abort(404, f"Post id {blog_id} doesn't exist")
    post = posts[0]
    if check_author and post.user_id != g.user.id:
        abort(403)

    return post


@bp.route("/<int:blog_id>/update", methods=("GET", "POST"))
@login_required
def update(blog_id: int):
    post = get_post(blog_id)

    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]

        if title is None:
            error = "Title is required"
            flash(error)
            return render_template("blog/update.html", post=post)

        blog_repository.update(blog_id, title, body)
        return redirect(url_for("blog.index"))

    return render_template("blog/update.html", post=post)


@bp.route("/<int:blog_id>/delete", methods=("POST",))
@login_required
def delete(blog_id: int):
    get_post(blog_id)
    blog_repository.delete_by_blog_id(blog_id)

    return redirect(url_for("blog.index"))
