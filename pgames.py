import telebot
import os
import pygame
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['sos'])
def help_message(message):
    bot.send_message(message.chat.id, text='сосиииии')


@bot.message_handler(commands=['games'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text='Весёлое кнутирование ;)',
                                                 url='https://t.me/Pizdoff_bot?game=Fun_and_whip')
    markup.row(button1)
    bot.send_message(message.chat.id, text="Приветик, {0.first_name}. Выбери игру!"
                     .format(message.from_user, bot.get_me()), parse_mode='markdown', reply_markup=markup)


bot.polling(none_stop=True, interval=0)
