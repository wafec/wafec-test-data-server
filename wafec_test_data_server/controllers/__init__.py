from .data_event_controller import data_event_controller

__all__ = [
    'register_controllers'
]


def register_controllers(app):
    app.register_blueprint(data_event_controller)