# _*_ coding: utf-8 _*_
import telebot
import constants

bot = telebot.TeleBot(constants.token)

@bot.message_handler(content_types=["commands"])
def handle_command(message):
    print('\n~~~~~~~~~~~~~~~~~~~')
    print("Пришла комманда")

@bot.message_handler(content_types=["text"])
def handle_text(message):
    print('\n~~~~~~~~~~~~~~~~~~~')
    print("Пришло сообщение")
    logs(message)

@bot.message_handler(content_types=["document"])
def handle_doc(message):
    print('\n~~~~~~~~~~~~~~~~~~~')
    print("Пришел документ")
    logs(message)

@bot.message_handler(content_types=["audio"])
def handle_audio(message):
    print('\n~~~~~~~~~~~~~~~~~~~')
    print("Пришло аудио")
    logs(message)

@bot.message_handler(content_types=["sticker"])
def handle_sticker(message):
    print('\n~~~~~~~~~~~~~~~~~~~')
    print("Пришел стикер")
    logs(message)

@bot.message_handler(content_types=["photo"])
def handle_photo(message):
    print('\n~~~~~~~~~~~~~~~~~~~')
    print("Пришло фото")
    logs(message)


def logs(message):
    from datetime import datetime
    date = datetime.now()
    print(date)
    print('Username: {0}'.format(message.chat.username))
    print('F_Name: {0}'.format(message.chat.first_name))
    print('L_Name: {0}'.format(message.chat.last_name))
    print('ID: {0}'.format(message.chat.id))
    print('Message: {0}'.format(message.text.encode('utf-8')))

bot.polling(none_stop=True, interval=0)