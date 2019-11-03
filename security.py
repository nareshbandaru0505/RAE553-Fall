# importing safe_str_cmp from werkzeug to compare strings
from werkzeug.security import safe_str_cmp
from user import User

#creating Users list
users = [
    User(1, 'naresh', 'naresh1234'),
    User(2, 'bandaru', 'bandaru1234'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)