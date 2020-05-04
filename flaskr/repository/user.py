from .db import query
from flaskr.model import User
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List, Optional


def find_user_by_name(username: str) -> List[User]:
    result = query("SELECT id, username, password FROM user WHERE username = ?", (username,))
    return [User(**u) for u in result]


def find_user_by_id(id_: int) -> List[User]:
    result = query("SELECT id, username, password FROM user WHERE id = ?", (id_,))
    return [User(*u) for u in result]


def register_user(username: str, password: str):
    query("INSERT INTO user (username, password) VALUES (?, ?)", (username, generate_password_hash(password),))


def check_match_password(username: str, password: str) -> Optional[User]:
    users = find_user_by_name(username)

    if len(users) == 0:
        return None
    user = users[0]
    db_password = user.password

    if check_password_hash(db_password, password):
        return user
    return None
