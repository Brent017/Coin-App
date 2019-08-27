import models

from flask import Blueprint, request, jsonify
from flask_login import current_user
from playhouse.shortcuts import model_to_dict # so that we can jsonify model and send back to client

coins = Blueprint('coin', 'coin', url_prefix="/coins/v1")

# Index route
@coins.route('/', methods=["GET"])
def get_all_coins():
	try:
		coins = [model_to_dict(coins) for coins in models.Coins.select()] #where(models.Coins.id == id)
		return jsonify(data=coins, status={"code": 200, "message": "Success!"})
	except models.DoesNotExist:
		return jsonify(data={}, status={"code": 401, "message": "Error getting resource"})

# Create route
@coins.route('/', methods=["POST"])
def create_coins():
	user = current_user.get_id() # get user
	# print(user, 'user')
	# print(type(user))
	# get payload and convert to dict
	payload = request.form.to_dict() # now we can read the json in py (like request.form to get form or request.files to get files)
	
	try:
		# print('beginning of try')
		# print('query: ', query)
		rows_from_coindb = [model_to_dict(row) for row in models.CoinDB.select().where(models.CoinDB.year == payload['year'], models.CoinDB.mintmark == payload['mint_mark'])]
		# print(query, '<--query')
		rows_filter_denom = []
		for row in rows_from_coindb:
			if row['denomination'] == float(payload['denomination']):
				rows_filter_denom.append(row)
		print('rows_filter_denom: ', rows_filter_denom)
		# loop through results of query
		for row_filter_denom in rows_filter_denom:
			payload['coindb'] = row_filter_denom['id']
			coin_dict = models.Coins.create(**payload, user=user)

		coin_list = [model_to_dict(coin) for coin in models.Coins.select().where(models.Coins.user == user)]
		print(coin_list, '<--coin_list')
		# for each result convert from model to dict, take id and result and add to payload and create each coin with same year, denom and mm but with different coindb_ids
		# print(payload, '<--payload in create')
		# print(payload, '<--payload in create')
		# get all coins
		# coins = [model_to_dict(coin_list) for coins in models.Coins.select().where(models.Coins.user == user)] #where(models.Coins.id == id)

		return jsonify(data=coin_list, status={"code": 201, "message": "Success!"})
	except models.DoesNotExist:
		return jsonify(data={}, status={"code": 401, "message": "Error getting resource"})


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




