from flask import Blueprint, Flask


health = Blueprint('health', __name__)


@health.route('/health', methods=['GET'])
def health_get():
    return 'Online', 200


def start(app: Flask):
    app.register_blueprint(health)
