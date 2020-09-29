from flask import Blueprint, request

__all__ = [
    'data_event_controller'
]


data_event_controller = Blueprint('data_event_controller', __name__)


@data_event_controller.route('/api/data_event/', methods=['POST'])
def post():
    print(request.data)
    return request.data
