from .db import query
from flaskr.model import UserBlog
from typing import List


def find_user_blog_by_blog_id(blog_id: int) -> List[UserBlog]:
    result = query(
        """
        SELECT p.id as blog_id, title as blog_title, body as blog_body, created as blog_created, 
               author_id as user_id, username
        FROM post AS p JOIN user AS u ON p.author_id = u.id
        WHERE p.id = ?
        """,
        (blog_id, )
    )

    return [
        UserBlog(**b) for b in result
    ]


def all() -> List[UserBlog]:
    result = query(
        """
        SELECT p.id as blog_id, title as blog_title, body as blog_body, created as blog_created,
               author_id as user_id, username
        FROM post AS p JOIN user AS u ON p.author_id = u.id
        ORDER BY blog_created DESC
        """
    )

    return [
        UserBlog(**b) for b in result
    ]
