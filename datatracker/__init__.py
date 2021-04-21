import os
from flask import Flask
from flask_bootstrap import Bootstrap


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config['MONGODB_SETTINGS'] = {
        "db" : "myapp",
    }

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import video_games
    app.register_blueprint(video_games.bp)
    # app.add_url_rule('/', endpoint='index')

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
