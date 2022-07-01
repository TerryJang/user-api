from flask import Flask
from router.main import main
from router.user import user

app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(user)


if __name__ == '__main__':
    app.run()
