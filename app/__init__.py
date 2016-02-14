from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.mongoengine import MongoEngine
from config import config

bootstrap = Bootstrap()
db = MongoEngine()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	bootstrap.init_app(app)
	db.init_app(app)

	from .main import questions as questions_blueprint
	app.register_blueprint(questions_blueprint)

	return app
