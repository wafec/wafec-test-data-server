from flask import Flask

from controllers import register_controllers


if __name__ == '__main__':
    app = Flask(__name__)
    register_controllers(app)
    app.run(host='0.0.0.0', port=9090)
