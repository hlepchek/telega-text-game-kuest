import telebot
from telebot import types
token="7192126500:AAH2rWLhNdhAD7nNh4xTrP7h0iP1s3JceIA"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def new_message(message):
    global msg
    msg = message.chat.id
    klaviature=types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bot.send_message(msg,"Сейчас мы с тобой поиграем в игру.")
    bot.send_message(msg,"Ты попадаешь в пещеру, здесь тебе нужно будет выбирать куда можно пойти.")
    bot.send_message(msg,"Твоя главная цель-найти бриллиант жизни.")
    bot.send_message(msg,"По пути  могут встретиться разные преграды, которые нужно будет преодолеть.")
    btn=types.KeyboardButton("далее")
    klaviature.add(btn)
    bot.send_message(msg,"Удачи!", reply_markup=klaviature)

@bot.message_handler(func=lambda message: message.text=='далее')
def next(message):
    klaviature = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn = types.KeyboardButton("путь справа")
    btn1 = types.KeyboardButton("путь слева")
    klaviature.add(btn,btn1)
    bot.send_photo(msg,photo=open("kartinki/putiN.png","rb"))
    bot.send_message(msg,"куда ты пойдешь?", reply_markup=klaviature)

    @bot.message_handler(func=lambda message: message.text=='путь справа')
    def vfvf(message):
        klaviature = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        btn2 = types.KeyboardButton("поставлю дощечку и перейду")
        btn3 = types.KeyboardButton("не буду искать брилиант")
        klaviature.add(btn2, btn3)
        bot.send_photo(msg,photo=open("kartinki/lava.jpeg","rb"))
        bot.send_message(msg, "Что ты будешь делать перед этой лавой?", reply_markup=klaviature)

        @bot.message_handler(func=lambda message: message.text=='поставлю дощечку и перейду')
        def flfl(message):
            klaviature = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            btn4=types.KeyboardButton("идти дальше")
            klaviature.add(btn4)
            bot.send_photo(msg, photo=open("kartinki/pehera.jpg","rb"))
            bot.send_message(msg, "пойдем?", reply_markup=klaviature)

            @bot.message_handler(func=lambda message: message.text == 'идти дальше')
            def glgll(message):
                bot.send_photo(msg,photo=open("kartinki/brilliant.jpeg","rb"))
                bot.send_message(msg, "поздравляю ты нашел брилиант.")

        @bot.message_handler(func=lambda message: message.text == 'не буду искать брилиант')
        def fofo(message):
            bot.send_photo(msg,photo=open("kartinki/esc.jpg","rb"))
            bot.send_message(msg, "ну что ж вот выход.Пока! ")

    @bot.message_handler(func=lambda message: message.text == 'путь слева')
    def trtr(message):
        klaviature = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        btn5=types.KeyboardButton("подраться с ним")
        btn6=types.KeyboardButton("убежать от страха")
        klaviature.add(btn5,btn6)
        bot.send_photo(msg,photo=open("kartinki/pauk.jpeg","rb"))
        bot.send_message(msg, "перед тобой монстр что ты будешь делать?", reply_markup=klaviature)

        @bot.message_handler(func=lambda message: message.text == 'подраться с ним')
        def eses(message):
            klaviature = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            btn7=types.KeyboardButton("идти вперед")
            klaviature.add(btn7)
            bot.send_photo(msg, photo=open("kartinki/-monstrik.jpg","rb"))
            bot.send_message(msg, "поздравляю, ты убил его, иди дальше.", reply_markup=klaviature)

            @bot.message_handler(func=lambda message: message.text == 'идти вперед')
            def nmnmnmn(message):
                bot.send_photo(msg,photo=open("kartinki/mister cherepah.jpg","rb"))
                bot.send_message(msg, "О нет! сзади тебя ЕЩЕ монстр! Пока пока!")

        @bot.message_handler(func=lambda message: message.text == 'убежать от страха')
        def zxzxzzxzx(message):
            bot.send_photo(msg, photo=open("kartinki/esc.jpg","rb"))
            bot.send_message(msg, "ну что ж, вот выход.Пока! ")

bot.polling(none_stop = True)