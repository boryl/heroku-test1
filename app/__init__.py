import os
from flask import Flask



def create_app():
	app = Flask(__name__)
	if(os.getenv('ENV') == 'PROD'):
		config = 'ProdConfig'
	else:
		config = 'DevConfig'
	
	app.config.from_object('config.' + config)
	
	with app.app_context():
		# Blueprints
		from . import routes
		
		app.register_blueprint(routes.main_bp)
		
		return app


