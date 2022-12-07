from ..database import Database
from os import getenv
from time import time
from argon2 import PasswordHasher
from authlib.jose import jwt, errors

ph = PasswordHasher()
access_token_secret_key = getenv('ACCESS_TOKEN_SECRET_KEY')
refresh_token_secret_key = getenv('REFRESH_TOKEN_SECRET_KEY')

class User:
    model = Database.dbInstance['uwc']['user']

    @staticmethod
    def register():
        pass

    @staticmethod
    def login(username: str, password: str) -> tuple[str | None, str] | None:
        if username is None or password is None:
            return None, 'Missing username or password'

        user = User.model.find_one({'username': username})

        if user is None:
            return None, 'User not found'

        try:
            ph.verify(user['password'], password)
        except:
            return None, 'User credentials not valid!'

        access_token = jwt.encode(
            header={
                'alg': 'HS256',
                'typ': 'JWT',
            },
            payload={
                'sub': '1',
                'name': user['username'],
                'role': user['role'],
                'exp': time() + (24 * 60 * 60), # 1 day
            },
            key=access_token_secret_key
        )

        return access_token.decode("utf-8"), ''
