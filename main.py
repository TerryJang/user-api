from flask import Flask

from router.main import main
from router.user import user
from router.auth_phone import auth_phone
from engine.mysql import mysql_connection_pool
from settings import get_config
from exception import register_error_handler

app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(user)
app.register_blueprint(auth_phone)


if __name__ == '__main__':
    config = get_config()
    mysql_connection_pool.setup(config=config)
    register_error_handler(app)
    app.run()
