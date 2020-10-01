from flask import Blueprint, request, jsonify

from wafec_test_data_server.models import *


__all__ = [
    'data_event_controller'
]


data_event_controller = Blueprint('data_event_controller', __name__)


@data_event_controller.route('/api/data_event/', methods=['POST'])
def post():
    session = Session()
    try:
        data_event = DataEvent()
        data_event.source = request.json['source']
        data_event.event_name = request.json['event_name']
        data_event.value = request.json['value']
        data_event.data_type = request.json['data_type']
        data_event.is_callable = request.json['is_callable']
        data_event.process_name = request.json['process_name']
        data_event.remote_addr = request.remote_addr
        session.add(data_event)
        session.commit()
        return jsonify({'id': data_event.id})
    except Exception as exc:
        session.rollback()
        return str(exc), 500
    finally:
        session.close()

