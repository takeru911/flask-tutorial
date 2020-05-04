from dataclasses import dataclass


@dataclass
class UserBlog:
    blog_id: int
    blog_title: str
    blog_body: str
    blog_created: str
    user_id: int
    username: str
