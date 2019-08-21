import models

from flask import Blueprint, request, jsonify
from flask_login import current_user
from playhouse.shortcuts import model_to_dict # so that we can jsonify model and send back to client

coins = Blueprint('coin', 'coin', url_prefix="/coins/v1")

# Index route
@coins.route('/', methods=["GET"])
def get_all_coins():
	try:
		coins = [model_to_dict(coins) for coins in models.Coins.select()]
		return jsonify(data=coins, status={"code": 200, "message": "Success!"})
	except models.DoesNotExist:
		return jsonify(data={}, status={"code": 401, "message": "Error getting resource"})

# Create route
@coins.route('/', methods=["POST"])
def create_coins():
	print(current_user, 'current_user')
	payload = request.get_json() # now we can read the json in py (like request.form to get form or request.files to get files)
	coins = models.Coins.create(**payload, user=1) # update to current_user 

	coins_dict = model_to_dict(coins)

	return jsonify(data=coins_dict, status={"code": 201, "message": "Success!"})

# Show route
@coins.route('/<id>', methods=["GET"])
def get_one_coin(id):
	coins = models.Coins.get_by_id(id)
	return jsonify(data=model_to_dict(coins), status={"code": 200, "message": "Success!"})

# Update route
@coins.route('/<id>', methods=["PUT"])
def update_coin(id):
	payload = request.get_json()

	query = models.Coins.update(**payload).where(models.Coins.id == id)
	query.execute()

	updated_coin = models.Coins.get_by_id(id)

	return jsonify(data=model_to_dict(updated_coin), status={"code": 200, "message": "Success!"})

# Delete route
@coins.route('/<id>', methods=["Delete"])
def delete_coin(id):
	query = models.Coins.delete().where(models.Coins.id == id)
	query.execute()
	
	return jsonify(data='resources successfully deleted', status={"code": 200, "message": "Resource deleted"})




