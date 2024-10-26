from flask import Blueprint, Flask


svc_accounts = Blueprint('svc_accounts', __name__)


@svc_accounts.route('/svc_accounts', methods=['GET'])
def get_svc_accounts():
    ...


@svc_accounts.route('/svc_accounts/new', methods=['POST'])
def add_svc_account():
    ...


@svc_accounts.route('/svc_accounts/update', methods=['POST'])
def update_svc_account():
    ...


@svc_accounts.route('/svc_accounts/delete', methods=['POST'])
def delete_svc_account():
    ...


def start(app: Flask):
    app.register_blueprint(svc_accounts)
