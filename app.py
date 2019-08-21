from flask import Flask, g
from flask_cors import CORS
from flask_login import LoginManager # import so users.py can use
import models

from api.users import user

DEBUG = True
PORT = 8000

login_manager = LoginManager() # set up ability to set up session

app = Flask(__name__, static_url_path="", static_folder="static")

app.secret_key = 'ALKERANDOM STRING' # encode our cookie
login_manager.init_app(app) # set up the session on the app

@login_manager.user_loader
def load_user(userid):
	try:
		return models.User.get(models.User.id == userid)
	except models.DoesNotExist:
		return None

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



