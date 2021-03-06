import os
from flask import Flask, g
from whitenoise import WhiteNoise
from flask_cors import CORS
from flask_login import LoginManager # import so users.py can use
import models

from api.users import user
from api.coins import coins

DEBUG = True
PORT = 8000

login_manager = LoginManager() # set up ability to set up session

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app, root=os.path.join(os.path.dirname(__file__), 'static'), prefix='static/')

app.secret_key = 'ALKERANDOM STRING' # encode our cookie
login_manager.init_app(app) # set up the session on the app

@login_manager.user_loader # load anything from the session (current_user) - function to define who the current user is
def load_user(userid):
	try:
		return models.User.get(models.User.id == userid)
	except models.DoesNotExist:
		return None

CORS(user, origins=['http://localhost:3000', 'http://coin-app-react.herokuapp.com', 'https://coin-app-react.herokuapp.com'], supports_credentials=True)
CORS(coins, origins=['http://localhost:3000', 'http://coin-app-react.herokuapp.com', 'https://coin-app-react.herokuapp.com'], supports_credentials=True)

app.register_blueprint(user)
app.register_blueprint(coins)

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

if 'ON_HEROKU' in os.environ:
	print('hitting ')
	models.initialize()

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)



