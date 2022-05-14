from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import sqlite3

#class for database

class Sql:
	def __init__(self):
		self.connection = sqlite3.connect('#name_of_your_database.db')
		self.cursor = self.connection.cursor()

	def baza(self):
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS user(
			id integer,
			username varchar(60),
			first_name varchar(60)
			)""")

	def user_add(self,idi,username,first_name):
		self.cursor.execute("INSERT INTO user (id,username,first_name) VALUES (?,?,?)",(idi,username,first_name))
		return self.connection.commit()

	#checking if this user is new in your bot
	def id_user(self,idi):
		self.cursor.execute(f"SELECT id FROM user WHERE id = {idi}")
		data = self.cursor.fetchone()
		return data
	
	#the counter of your users
	def userlar(self):
		self.cursor.execute(f"SELECT COUNT(id) FROM user")
		info = self.cursor.fetchall()
		r = None
		for i in info:
			r = i[0]
		return r
	
	#the list of telegram_ids of your bot users
	def rec(self):
		self.cursor.execute(f"SELECT * FROM user")
		idila = self.cursor.fetchall()		
		return idila


menu1 = InlineKeyboardMarkup(
	inline_keyboard= [
		[
		InlineKeyboardButton(text="🇷🇺 Russian",callback_data="ru"),
		InlineKeyboardButton(text="🇬🇧 English",callback_data="en")
		],
		[
		InlineKeyboardButton(text="🇺🇿 Uzbekcha",callback_data="uz"),
		InlineKeyboardButton(text="🇸🇦 Arabic",callback_data="ar")
		],
		[
		InlineKeyboardButton(text="🇪🇸 Spanish",callback_data="es"),
		InlineKeyboardButton(text="🇫🇷 French",callback_data="fr")
		],
		[
		InlineKeyboardButton(text="🇯🇵 Japanese",callback_data="ja"),
		InlineKeyboardButton(text="🇰🇷 Korean",callback_data="ko")
		],
		[
		InlineKeyboardButton(text="🇹🇷 Turkish",callback_data="tr"),
		InlineKeyboardButton(text="🇮🇹 Italian",callback_data="it")
		],
		[
		InlineKeyboardButton(text="🇮🇳 Hindi",callback_data="hi"),
		InlineKeyboardButton(text="🇩🇪 German",callback_data="de")
		],
		[
		InlineKeyboardButton(text="Latin",callback_data="la"),
		InlineKeyboardButton(text="🇵🇹 Portuguese",callback_data="pt")
		],
		[
		InlineKeyboardButton(text="🇺🇦 Ukrainian",callback_data="uk"),
		InlineKeyboardButton(text="🇨🇿 Czech",callback_data="cs")
		],
		[
		InlineKeyboardButton(text="🇨🇳 Chinese",callback_data="zh-cn"),
		InlineKeyboardButton(text="🇮🇸 Icelandic",callback_data="is")
		],
	]
)