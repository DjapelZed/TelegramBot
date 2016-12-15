# _*_ coding: utf-8 _*_
from telebot import TeleBot
import constants

bot = TeleBot(constants.token)


@bot.message_handler(commands=['start'])
def handle_start(message):
    print('\n~~~~~~~~~~~~~~~~~~~')
    print('New SESSION')
    print("Received a COMMAND")
    bot.send_message(message.chat.id, 'Чем могу помочь?')
    logs(message)
    log_mess(message)


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id,
                     'Привет!\n'
                     'Это я, Питончик (оригинальное имя для меня придумали однако)!\n'
                     '{0}, если у тебя есть оригинальные идеи как бы меня усовершенствовать, то пиши Максиму ('
                     '@kushnirov)\n '
                     'Я еще маленький, но я буду расти.\n'
                     'Если ты хочешь помочь моему создателю (не материально, '
                     'а умственно (разрабатывать меня(да, это скобки в скобках))), то пиши Максу(@kushnirov)\n'
                     '🐍🐍🐍🐍🐍🐍'.format(message.chat.first_name))


@bot.message_handler(commands=['translate'])
def handle_translate(message):
    print('\n~~~~~~~~~~~~~~~~~~~')
    print("COMMAND TRANSLATE")
    if message.text == '/translate' and constants.translate:
        print('Translate mode OFF')
        bot.send_message(message.chat.id, 'Режим переводчика выключен!')
        constants.translate = False
    elif message.text == '/translate':
        constants.translate = True
        print('Translate mode ON')
        bot.send_message(message.chat.id, 'Переведено сервисом «Яндекс.Переводчик»\n'
                                          'http://translate.yandex.ru/')
        bot.send_message(message.chat.id, 'Ты активировал режим переводчика!\n'
                                          'Теперь просто вводи текст на русском, а я буду присылать такой же текст на '
                                          'английском. Еще ты можешь прислать документ, который необходимо перевести '
                                          'Чтобы выключить режим переводчика вбей еще раз эту комманду - /translate')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    print('\n~~~~~~~~~~~~~~~~~~~')
    print("Message")
    logs(message)
    if constants.translate:
        translate(message)
    if message.text:
        log_mess(message)


@bot.message_handler(content_types=["document"])
def handle_doc(message):
    print('\n~~~~~~~~~~~~~~~~~~~')
    print("Received a DOCUMENT")
    logs(message)


@bot.message_handler(content_types=["audio"])
def handle_audio(message):
    print('\n~~~~~~~~~~~~~~~~~~~')
    print("Received an AUDIO")
    logs(message)


@bot.message_handler(content_types=["sticker"])
def handle_sticker(message):
    print('\n~~~~~~~~~~~~~~~~~~~')
    print("Received a STICKER")
    logs(message)


@bot.message_handler(content_types=["photo"])
def handle_photo(message):
    print('\n~~~~~~~~~~~~~~~~~~~')
    print("Received a PHOTO")
    logs(message)
    if message.photo:
        log_photo(message)


# ~~~~~~~~~~~~~~COMMANDS~~~~~~~~~~~~~~~




# ~~~~~~~~~~~~~TRANSLATE~~~~~~~~~~~~~~~
def translate(message):
    if constants.translate:
        import requests
        import json
        url = constants.url
        key = constants.key
        text = message.text
        lang = 'ru-en'
        r = requests.post(url, data={'key': key, 'text': text, 'lang': lang})
        # Выводим результат
        string = json.loads(r.text)
        bot.send_message(message.chat.id, string['text'])
        print('Answer: {0}'.format(string['text'][0]))


# ~~~~~~~~~~~~~~~LOG~~~~~~~~~~~~~~~~~~
def log_photo(message):
    print('File_ID: {0}'.format(message.photo[1].file_id))
    print('Photo_Size(WxH): {0}x{1}'.format(message.photo[1].width, message.photo[1].height))
    print('Photo_Size: {0}'.format(message.photo[0].file_size))


def log_mess(message):
    print('Message: {0}'.format(message.text.encode('utf-8').decode()))


def logs(message):
    from datetime import datetime
    date = datetime.now()
    print(date)
    print('Username: {0}'.format(message.chat.username))
    print('F_Name: {0}'.format(message.chat.first_name))
    print('L_Name: {0}'.format(message.chat.last_name))
    print('ID: {0}'.format(message.chat.id))


bot.polling(none_stop=True, interval=0)
