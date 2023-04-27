import telebot
import config
import random
import re
from Parse_converter import get_url
from telebot import types

bot = telebot.TeleBot(config.TOKEN)
dict_1 = '''Декогере́нция — это процесс нарушения когерентности (от лат. cohaerentio — сцепление, связь), вызываемый взаимодействием квантовомеханической системы с окружающей средой посредством необратимого с точки зрения термодинамики процесса. Проще говоря, это нарушение изоляции системы - контакт с наблюдателем.\n
Теория Хью Эверетта - Концепция о расщеплении и ветвлении миров заключается в следующем: при любом акте измерения реально осуществляются, с той или иной вероятностью, все возможные исходы этого измерения. Но каждый вариант осуществляется в «своей вселенной», отличающейся от всех прочих именно этим исходом, т.е. состоянием памяти наблюдателя, видящего определённый исход измерения. Реально существуют (хотя и не взаимодействуют друг с другом) все решения волновых уравнений и все варианты состояния наблюдателя-человека, отличающиеся находящимся в его памяти результатом измерения. Каждый из этих вариантов состояния подсистемы-наблюдателя является «соотнесённым состоянием», связанным с тем или иным состоянием наблюдаемой подсистемы.\n
Многомирова́я интерпрета́ция (англ. many-worlds interpretation) или интерпретация Эверетта — интерпретация квантовой механики, которая предполагает существование, в некотором смысле, «параллельных вселенных», в каждой из которых действуют одни и те же законы природы и которым свойственны одни и те же мировые постоянные, но которые находятся в различных состояниях.\n
'''


@bot.message_handler(commands=['start'])
def welcome(message):
    stick = open('Monkey_potty.mp4', 'rb')
    bot.send_video(message.chat.id, stick)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲Проверить свою удачу🎲")
    item2 = types.KeyboardButton("📕Словарь📕")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!\nТы можешь задать свой вопрос в формате "Что такое (любой термин)?"'.format(message.from_user),
                     parse_mode='html',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    global i1, dict_1
    if message.chat.type == 'private':
        if message.text == "🎲Проверить свою удачу🎲":
            life = random.choice([True, False])
            bot.send_message(message.chat.id, 'Вы выжили' if life else 'Вы умерли')
        elif message.text == "📕Словарь📕":
            bot.send_message(message.chat.id, dict_1)
        elif re.findall(r'[Чч]то\s+?(значит)|(такое)\s+?\w+', message.text):
            bot.send_message(message.chat.id, get_url(message.text + "wikipedia"))
        else:
            bot.send_message(message.chat.id, "Я вас не понял, попробуйте задать вопрос по-другому")



bot.polling(none_stop=True)
