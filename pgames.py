import telebot
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, text ='сосиииии')

@bot.message_handler(commands=['games'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Открыть канал armandpzdoff', url = 'https://www.twitch.tv/armandpzdoff'))
    markup.add(telebot.types.InlineKeyboardButton(text='Расписание трансляций', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='Сборник клипов с канала', url = 'https://www.twitch.tv/armandpzdoff/clips?filter=clips&range=all'))
    markup.add(telebot.types.InlineKeyboardButton(text='Последние клипы (7 дней)',url = 'https://www.twitch.tv/armandpzdoff/clips?filter=clips&range=7d'))
    bot.send_message(message.chat.id,
                     text="*Приветик, {0.first_name}, мой дорогой зритель!*\n"
                          "Я оповещаю чат о начале трансляций на канале https://www.twitch.tv/armandpzdoff\n"                         
                          "Так же Вы можете выбрать интересующий раздел меню".format(message.from_user, bot.get_me()), parse_mode='markdown', reply_markup=markup)
#.format(message.chat.id)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id)
    if call.data == '1':
        bot.send_message(call.message.chat.id, text="Стабильного расписания пока нет :(")

bot.polling(none_stop=True, interval=0)