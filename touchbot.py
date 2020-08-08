

import os
import telebot
BOT_API_TOKEN = "1376743466:AAHX5y87-h7BtqnSmnX2Sa1G61eAnShddrI"
bot = telebot.TeleBot(BOT_API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message)
    id = message.from_user.id
    bot.send_message(chat_id=id, text="Hello, loving this work, how about you?!")

@bot.message_handler(commands=['help'])
def hanle_start_help(message):
    print(message)
    id = message.from_user.id
    bot.send_message(chat_id=id, text="How may i help you? !")

@bot.message_handler(commands=['photo'])
def handle_docs_photo(message):
    print(message)
    id = message.from_user.id
    bot.send_photo(chat_id=id, photo="https://st.depositphotos.com/1001024/1489/i/950/depositphotos_14895357-stock-photo-spy-girl-in-a-black.jpg")

@bot.message_handler(commands=['view'])
def handle_docs_photo(message):
    print(message)
    id = message.from_user.id 
    bot.send_photo(chat_id=id, photo="https://i.ytimg.com/vi/1yBwWLunlOM/maxresdefault.jpg")

@bot.message_handler(commands=['audio'])
def handle_docs_audio(message):
    print(message)
    id = message.from_user.id 
    bot.send_audio(chat_id=id, audio="https://d274.cdn-me.net/c.php?s=eNoBSAC3%252FxndCFp8AkwbS%252B%252BFg6MUFKELU7rwQOvVjfUnU43bqkvYNpE2vzK4NMJ67bluLrXOPJgGrGOPGtKQSVyeFMmuZSk8lKagndn5H8MYIvQ%253D")

@bot.message_handler(commands=['video'])
def handle_docs_video(message):
    print(message)
    id = message.from_user.id 
    bot.send_video(chat_id=id, data="https://res.cloudinary.com/loving-the-work/video/upload/v1596886945/davido_d_g_official_video_ft._summer_walker_h264_42011_uct21k.mp4")



bot.polling()