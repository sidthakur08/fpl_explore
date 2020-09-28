from flask import Flask
from config import Config

def init_app(config_class=Config):
    app = Flask(__name__, template_folder='template')
    # configuration
    app.config.from_object(config_class)

    with app.app_context():
        from . import routes
        from fpl.dashboard.keeper import init_keeper
        app = init_keeper(app)
        from fpl.dashboard.defender import init_defender
        app = init_defender(app)
        from fpl.dashboard.attacker import init_attacker
        app = init_attacker(app)
        return app