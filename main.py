from flask import Flask
from router.main import main
from router.user import user
from engine.mysql import mysql_connection_pool
from settings import get_config

app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(user)


if __name__ == '__main__':
    config = get_config()
    mysql_connection_pool.setup(config=config)
    app.run()
