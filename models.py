from peewee import *
from flask_login import UserMixin

# DATABASE = SqliteDatabase('coin.sqlite')
DATABASE = PostgresqlDatabase('coins')

class User(UserMixin, Model):
	username = CharField()
	email = CharField()
	password = CharField()
	image = CharField()

	class Meta:
		database = DATABASE

class Coins(Model):
	year = CharField(null = True)
	denomination = CharField(null = True)
	mint_mark = CharField(null = True)
	number_minted = CharField(null = True)
	composition = CharField(null = True)
	melt_value = CharField(null = True)
	num_value = CharField(null = True)
	user = ForeignKeyField(User, backref='coins')

	class Meta:
		database = DATABASE

class CoinDB(Model):
	denomination = FloatField()
	year = FloatField()
	mintmark = CharField()
	description = CharField()
	total_mintage = CharField()
	proof_mintage = CharField()
	comments = CharField()

	class Meta:
		database = DATABASE

def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User, Coins, CoinDB], safe=True)
	print("TABLES CREATED")
	DATABASE.close()



