from googletrans import Translator
from config import *
import logging
from buttons import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
w = Sql()
a = Translator()

Admin = #your telegram id

#============== Entry ===================

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
	w.baza()
	user_id = message.from_user.id
	username = message.from_user.username
	first_name = message.from_user.first_name
	data1 = w.id_user(user_id)
	if data1 is None:
		w.user_add(user_id,username,first_name)
		await message.answer(f"Мы рады видеть вас здесь!\nПожалуйста, отправьте текст, который вы хотите перевести:")
		await bot.send_message(Admin,f"✅ Новый пользователь: \nusername: @{message.from_user.username}\nid: {message.from_user.id}\nИмя: {message.from_user.first_name}")
	else:
		await message.answer(f"Пожалуйста, отправьте текст, который вы хотите перевести:")

#=================  Commands for Administration ================================

@dp.message_handler(commands=['allusers'])
async def send_welcome(message: types.Message):
	p = w.userlar()
	await bot.send_message(Admin,f"The quantity of users: {p}")

@dp.message_handler(commands=['ads'],user_id=Admin)
async def send_welcome(message: types.Message):
	q = w.rec()
	e = message.text[5::]
	for k in q:
		data2 = k[0]
		await bot.send_message(chat_id=data2,text=e)

#============= The main part of the bot ====================

@dp.message_handler()
async def echo(message: types.Message):
    global t
    t = message.text  
    await message.answer("🔎Выберите язык для перевода:",reply_markup=menu1)

#============= List of code for translate ==================

@dp.callback_query_handler(text='ru')
async def func(call:CallbackQuery):
	x = a.translate(t, dest = 'ru')
	await call.message.answer(x.text)

@dp.callback_query_handler(text='en')
async def func(call:CallbackQuery):
	x = a.translate(t, dest='en')
	await call.message.answer(x.text)

@dp.callback_query_handler(text='uz')
async def func(call:CallbackQuery):
	x = a.translate(t, dest='uz')
	await call.message.answer(x.text)

@dp.callback_query_handler(text='ar')
async def func(call:CallbackQuery):
	x = a.translate(t, dest='ar')
	await call.message.answer(x.text)

@dp.callback_query_handler(text='es')
async def func(call:CallbackQuery):
	x = a.translate(t, dest='es')
	await call.message.answer(x.text)

@dp.callback_query_handler(text='fr')
async def func(call:CallbackQuery):
	x = a.translate(t, dest='fr')
	await call.message.answer(x.text)

@dp.callback_query_handler(text='ja')
async def func(call:CallbackQuery):
	x = a.translate(t, dest='ja')
	await call.message.answer(x.text)

@dp.callback_query_handler(text='ko')
async def func(call:CallbackQuery):
	x = a.translate(t, dest='ko')
	await call.message.answer(x.text)

@dp.callback_query_handler(text='tr')
async def func(call:CallbackQuery):
	x = a.translate(t, dest='tr')
	await call.message.answer(x.text)

@dp.callback_query_handler(text='it')
async def func(call:CallbackQuery):
	x = a.translate(t, dest='it')
	await call.message.answer(x.text)

@dp.callback_query_handler(text='hi')
async def func(call:CallbackQuery):
	x = a.translate(t, dest='hi')
	await call.message.answer(x.text)

@dp.callback_query_handler(text='de')
async def func(call:CallbackQuery):
	x = a.translate(t, dest='de')
	await call.message.answer(x.text)

@dp.callback_query_handler(text='la')
async def func(call:CallbackQuery):
	x = a.translate(t, dest='la')
	await call.message.answer(x.text)

@dp.callback_query_handler(text='pt')
async def func(call:CallbackQuery):
	x = a.translate(t, dest='pt')
	await call.message.answer(x.text)

@dp.callback_query_handler(text='uk')
async def func(call:CallbackQuery):
	x = a.translate(t, dest='uk')
	await call.message.answer(x.text)

@dp.callback_query_handler(text='cs')
async def func(call:CallbackQuery):
	x = a.translate(t, dest='cs')
	await call.message.answer(x.text)

@dp.callback_query_handler(text='is')
async def func(call:CallbackQuery):
	x = a.translate(t, dest='is')
	await call.message.answer(x.text)

@dp.callback_query_handler(text='zh-cn')
async def func(call:CallbackQuery):
	x = a.translate(t, dest='zh-cn')
	await call.message.answer(x.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)