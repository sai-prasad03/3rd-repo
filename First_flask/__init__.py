from flask import Flask


def create_app():
    app = Flask(__name__)

    from First_flask.user.views import mod as users_module

    app.register_blueprint(users_module)

    return app
