from peewee import *
from flask_login import UserMixin

DATABASE = SqliteDatabase('coin.sqlite')

class User(UserMixin, Model):
	username = CharField()
	email = CharField()
	password = CharField()
	image = CharField()

	class Meta:
		database = DATABASE

class Coins(Model):
	year = CharField()
	denomination = CharField()
	mint_mark = CharField()
	number_minted = CharField()
	composition_primary = CharField()
	percent_primary = CharField()
	composition_secondary = CharField()
	percent_secondary = CharField()
	melt_value = CharField()
	num_value = CharField()
	user = ForeignKeyField(User, backref='coins')

	class Meta:
		database = DATABASE


def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User, Coins], safe=True)
	print("TABLES CREATED")
	DATABASE.close()



