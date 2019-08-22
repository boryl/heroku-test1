from flask import current_app as app
from flask import Blueprint, make_response, jsonify
import os

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def home():
	output = 'ENV: ' + app.config['ENV']
	output += '<br>CUSTOM_BASE: ' + app.config['CUSTOM_BASE']
	output += '<br>CUSTOM: ' + app.config['CUSTOM']
	output += '<br>SQLALCHEMY_DATABASE_URI: ' + app.config['SQLALCHEMY_DATABASE_URI']
	
	
	return output

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)
		
@app.errorhandler(400)
def not_found(error):
	return make_response(jsonify({'error': 'Bad request'}), 400)