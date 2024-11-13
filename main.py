from random import randint, random
import telebot
from telebot import types

TOKEN = "7971341692:AAFEaRM5Ng9_lQ5xtzQ0VNwJZkRqdfzMB2M"

bot = telebot.TeleBot(TOKEN)
random_bot = ["","ножницы", "бумагу", "камень"]
markup = types.ReplyKeyboardMarkup()

@bot.message_handler(commands=['start'])
def main(message):
    bt1 = types.KeyboardButton('ножницы')
    bt2 = types.KeyboardButton('бумага')
    bt3 = types.KeyboardButton('камень')
    markup.row(bt1)
    markup.row(bt2)
    markup.row(bt3)
    bot.send_message(message.chat.id, f'Давай поиграем {message.from_user.username}!', reply_markup=markup)
    bot.register_next_step_handler(message, reply_markup_button)

@bot.message_handler()
def reply_markup_button(message):
    a = random_bot[randint(1, 3)]
    if message.text == 'ножницы':
        if a == "ножницы":
            bot.send_message(message.chat.id, f'Я кидаю: {a}, ничья!')
        elif a == "бумага":
            bot.send_message(message.chat.id, f'Я кидаю: {a}, ты победил!')
        elif a == "камень":
            bot.send_message(message.chat.id, f'Я кидаю: {a}, я победил!')
    elif message.text == 'бумага':
        if a == "ножницы":
            bot.send_message(message.chat.id, f'Я кидаю: {a}, я победил!')
        elif a == "бумага":
            bot.send_message(message.chat.id, f'Я кидаю: {a}, ничья!')
        elif a == "камень":
            bot.send_message(message.chat.id, f'Я кидаю: {a}, ты победил!')
    elif message.text == 'камень':
        if a == "ножницы":
            bot.send_message(message.chat.id, f'Я кидаю: {a}, ты победил!')
        elif a == "бумага":
            bot.send_message(message.chat.id, f'Я кидаю: {a}, я победил!')
        elif a == "камень":
            bot.send_message(message.chat.id, f'Я кидаю: {a}, ничья!')


bot.polling(non_stop=True)