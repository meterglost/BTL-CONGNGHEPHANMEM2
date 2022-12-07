import secrets

env = {
    "COMPOSE_PROJECT_NAME": "BTL-CONGNGHEPHANMEM",
    "TZ": "Asia/Ho_Chi_Minh",
    "ACCESS_TOKEN_SECRET_KEY": secrets.token_hex(32),
    "REFRESH_TOKEN_SECRET_KEY": secrets.token_hex(32),
    "MONGO_INITDB_ROOT_USERNAME": "root",
    "MONGO_INITDB_ROOT_PASSWORD": secrets.token_urlsafe(16),
}

try:
    with open('.env', 'xt') as f:
        for key in env.keys():
            f.write(key + '=' + env[key] + '\n')
except:
    print('.env file existed!')
