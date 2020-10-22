from flask import Flask

from python_clean_architecture.rest import orderdata
from python_clean_architecture.settings import DevConfig


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(orderdata.blueprint)
    return app