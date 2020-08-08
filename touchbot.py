

import os
import telebot
BOT_API_TOKEN = "BOT FROM BOTFATHER"
bot = telebot.TeleBot(BOT_API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message)
    id = message.from_user.id
    bot.send_message(chat_id=id, text="!")

@bot.message_handler(commands=['help'])
def hanle_start_help(message):
    print(message)
    id = message.from_user.id
    bot.send_message(chat_id=id, text="!")

@bot.message_handler(commands=['photo'])
def handle_docs_photo(message):
    print(message)
    id = message.from_user.id
    bot.send_photo(chat_id=id, photo="")

@bot.message_handler(commands=['view'])
def handle_docs_photo(message):
    print(message)
    id = message.from_user.id 
    bot.send_photo(chat_id=id, photo="")

@bot.message_handler(commands=['audio'])
def handle_docs_audio(message):
    print(message)
    id = message.from_user.id 
    bot.send_audio(chat_id=id, audio="")

@bot.message_handler(commands=['video'])
def handle_docs_video(message):
    print(message)
    id = message.from_user.id 
    bot.send_video(chat_id=id, data="")



bot.polling()
