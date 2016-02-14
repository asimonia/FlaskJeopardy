import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	MONGODB_SETTINGS = {"DB": "jeopardy"}
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'KeepThisS3cr3t'

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True

config = {
	'development': DevelopmentConfig,
	'default': DevelopmentConfig
}