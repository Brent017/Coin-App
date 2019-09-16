from peewee import *
from flask_login import UserMixin
import os
from playhouse.db_url import connect

# DATABASE = SqliteDatabase('coin.sqlite')
DATABASE = PostgresqlDatabase('coins')
# DATABASE = connect(os.environ.get('DATABASE_URL'))

class CoinDB(Model):
	denomination = FloatField()
	year = IntegerField()
	mintmark = CharField()
	description = CharField()
	total_mintage = CharField()
	proof_mintage = CharField()
	comments = CharField()

	class Meta:
		database = DATABASE

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
	coindb = ForeignKeyField(CoinDB, backref='coindb')

	class Meta:
		database = DATABASE
# test
def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User, Coins, CoinDB], safe=True)
	print("TABLES CREATED")
	DATABASE.close()



