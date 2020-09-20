from flask import Flask

def init_app():
    app = Flask(__name__,instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        from . import routes

        from .dashboard.dash_app import init_dashboard
        app = init_dashboard(app)

        return app