from .db import query


def post_blog(title: str, body: str, user_id: str):
    query(
        "INSERT INTO POST (title, body, author_id) VALUES(?, ?, ?)",
        (title, body, user_id)
    )


def update(blog_id: int, update_title: str, update_body: str):
    query(
        "UPDATE post SET title = ?, body = ? WHERE id = ?",
        (update_title, update_body, blog_id,)
    )


def delete_by_blog_id(blog_id: int):
    query(
        "DELETE FROM post WHERE id = ?",
        (blog_id,)
    )
