from flask import Flask

from account_service.controllers.accounts import accounts
from account_service.controllers.health import health
from account_service import setup_swagger, SWAGGER_URL


def create(account_repository, customer_client):
    app = Flask(__name__)

    app.account_repository = account_repository
    app.customer_client = customer_client

    app.register_blueprint(health)
    app.register_blueprint(accounts)

    app.register_blueprint(setup_swagger(), url_prefix=SWAGGER_URL)

    return app
