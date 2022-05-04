import telebot
from telebot import types

bot = telebot.TeleBot('')#Token

@bot.message_handler(commands=['start'])
def start_welcome(message):
	bot.reply_to(message, "Привет! Введи число Fibonacci.")

@bot.message_handler()
def get_user_text(message):
	F1 = 1
	F2 = 1
	if message.text.isdigit():
		while int(message.text) > F2:
			F1, F2 = F2, F1 + F2
		if int(message.text) == F2:
			bot.reply_to(message, F1 + F2)
		elif int(message.text) == 0:
			bot.reply_to(message, "Веди число Fibonacci, оно должно быть больше 2")
		else:
			bot.reply_to(message, "Число не в ряду Fibonacci")

bot.polling(none_stop=True)