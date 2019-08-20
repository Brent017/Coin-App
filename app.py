from flask import Flask, g
from flask_cors import CORS
import models

from api.users import user

DEBUG = True
PORT = 8000

# login_manager = LoginManager()

app = Flask(__name__)


CORS(user, origins=['httpd://localhost:3000'], supports_credentials=True)
# CORS(coins, origins=['httpd://localhost:3000'], supports_credentials=True)

app.register_blueprint(user)
# app.register_blueprint(coins)

@app.before_request
def before_request():
	"""Connect to database before each request"""
	g.db = models.DATABASE
	g.db.connect()

@app.after_request
def after_request(response):
	###Close the database connection after each request###
	g.db.close()
	return response

app.route('/')

def index():
	return 'hi'

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)



