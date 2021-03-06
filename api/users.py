import models

import os
import sys
import secrets
from PIL import Image

from flask import Blueprint, request, jsonify, url_for, send_file 
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user
from playhouse.shortcuts import model_to_dict

user = Blueprint('users', 'user', url_prefix='/user')

# Save picture
def save_picture(form_picture): # funct to save image as static asset
	random_hex = secrets.token_hex(8) # generate random name so we dont have any conflicts
	f_name, f_ext = os.path.splitext(form_picture.filename) # grab the file name and ext (jpg) keep same ext and gives access to os filepaths. =>['brentProfile', 'jpg']
	picture_name = random_hex + f_ext 
	file_path_for_avatar = os.path.join(os.getcwd(), 'static/profile_pics/' + picture_name) # create file path
	# PIL code starts
	output_size = (125, 175) # size in px (tuple)
	i = Image.open(form_picture) # i is Image class from PIL import Image
	i.thumbnail(output_size) # set size accepts a tuple with dimensions
	i.save(file_path_for_avatar) # save path
	return picture_name

# Login
@user.route('/login', methods=["POST"])
def login():
	payload = request.get_json();
	print(payload, '<-payload in login')
	try:
		user = models.User.get(models.User.username == payload['username']);
		user_dict = model_to_dict(user)
		if(check_password_hash(user_dict['password'], payload['password'])):
			del user_dict['password']
			login_user(user)
			print(user, '<-user in login')
			return jsonify(data=user_dict, status={"code": 201, "message": "Success!"})
		else:
			return jsonify(data={}, status={"code": 401, "message": "Username or Password incorrect. Please try again or Register now."})
	except models.DoesNotExist:
		return jsonify(data={}, status={"code": 401, "message": "Username or Password incorrect. Please try again or Register now."})

# Register
@user.route('/register', methods=["POST"])
def register():
	pay_file = request.files
	payload = request.form.to_dict()
	dict_file = pay_file.to_dict()

	print(payload, 'payload')
	print(dict_file)

	payload['email'].lower()
	try:
		models.User.get(models.User.email == payload['email']) # make sure pw does not exist
		return jsonify(data={}, status={"code": 401, "message": "A user with that name or email already exists"})
	except models.DoesNotExist:
		payload['password'] = generate_password_hash(payload['password']) # hash pw
		file_picture_path = save_picture(dict_file['file']) # funct to save static asset
		payload['image'] = file_picture_path # add the image property to the payload_dict & save path in db
		user = models.User.create(**payload) # create the row in the sql table
		print(type(user)) 

		login_user(user) # start the user session, set userid in sessions
		current_user.image = file_picture_path # and the pic so we can have whenever

		user_dict = model_to_dict(user)
		# print(user_dict)
		# print(type(user_dict))

		del user_dict['password'] # remove pw, client doesnt need
		return jsonify(data=user_dict, status={"code": 201, "message": "Success!"})

@user.route('<id>/coins', methods=["GET"])
def get_user_coins(id):
	user = models.User.get_by_id(id)
	print(user.coins, "coindb")

	# for i in user.coins:
	# 	print(model_to_dict(i)) # this is every coin
	# same as above just cleaner, looping over coins of user
	coins = [model_to_dict(coins) for coins in user.coins]

	def delete_key(item, key): # removes user info from return
		del item[key]
		return item

	coins_without_user = [delete_key(coins, 'user') for coins in coins]

	return jsonify(data=coins, status={"code": 201, "message": "Success!"})

# Logout
@user.route('/logout')
def logout():
	logout_user()
	return redirect('/login')



	