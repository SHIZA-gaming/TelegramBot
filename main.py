import telebot
import const
import os
import urllib.request as urllib2

bot = telebot.TeleBot(const.token)


# upd = bot.get_updates()
# print(upd)
#
# last_upd = upd[-1]
# message_from_user = last_upd.message
# print(message_from_user)
# print(bot.get_me())


def log(message, answer):
    print("\n ----")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print(answer)


@bot.message_handler(commands=["start"])
def heandle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row("/start", "/stop")
    user_markup.row("IPhone 12", "IPhone 12 mini")
    user_markup.row("IPhone 12 Pro", "IPhone 12 Pro Max")
    user_markup.row("IPhone 11", "IPhone 11 Pro")
    user_markup.row("IPhone 11 Pro Max", "IPhone XS Max")
    user_markup.row("IPhone X", "IPhone XS", "IPhone XR")
    user_markup.row("IPhone", "IPhone SE")
    bot.send_message(message.chat.id, "Выбери свой АЙФОН", reply_markup=user_markup)
#Клавиатура. чтобы она появилась и ее содержание

@bot.message_handler(commands=["stop"])
def heandle_stop(message):
    remove_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,  "Мы закончили?... Ладно...(", reply_markup=remove_markup)
#Убрать клавиаткуру

@bot.message_handler(commands=["help"])
def heandle_help(message):
    bot.send_message(message.chat.id, """Мои возможности весьма спецефичны, но, ты тоько псомотри!
    Всё работает!!!""")
#Команда /help

@bot.message_handler(content_types=['text'])
def heandle_text(message):
    if message.text == "IPhone 12":
        directory = "C:/Users/g.chistopolskij/github/TelegramBot/photo/"
        IP12img = open(directory + "IP12.jfif", 'rb')
        IP12text = "IPhone 12 есть в 5 цветах: Black(осуждаю!), White, Green, Blue, (PRODUCT) Red.\nКупи IPhone 12 всего лишь за 80.000 рублей"
        markup = types.InlineKeyboardMarkup(row_width=2)
        option1 = types.InlineKeyboardButton("Купить", callback_data='buy')
        option2 = types.InlineKeyboardButton("Не покупать", callback_data='dont buy')
        markup.add(option1, option2)
        bot.send_photo(message.from_user.id, IP12img)
        bot.send_message(message.chat.id, IP12text, reply_markup=markup)
        bot.send_message(message.chat.id, "https://www.apple.com/ru/shop/buy-iphone/iphone-12")

    elif message.text == "IPhone 12 mini":
        directory = "C:/Users/g.chistopolskij/github/TelegramBot/photo/"
        IP12MINIimg = open(directory + "mini.jpeg", 'rb')
        IP12MINItext = "IPhone 12 mini есть в 5 цветах: Black(осуждаю!), White, Green, Blue, (PRODUCT) Red.\nКупи IPhone 12 mini всего за какие-то жалкие 70.000 рублей.\n\
https://www.apple.com/ru/shop/buy-iphone/iphone-12"
        bot.send_photo(message.from_user.id, IP12MINIimg)
        bot.send_message(message.chat.id, IP12MINItext)
    elif message.text == "IPhone 12 Pro":
        directory = "C:/Users/g.chistopolskij/github/TelegramBot/photo/"
        IP12PROimg = open(directory + "IP12PRO.jfif", 'rb')
        IP12PROtext = "IPhone 12 Pro есть в 4 цветах: Graphite, Silver, Gold, Pacific Blue\n Купи IPhone 12 Pro всего за 100.000 рублей\n\
https://www.apple.com/ru/shop/buy-iphone/iphone-12-pro"
            # img.close()
        # bot.send_message(message.chat.id, f'{IP12img}\n{IP12text}')
#elif message.text == "IPhone 11"
        # bot.send_message(message.chat.id, f'{IP12img}\n{IP12text}')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'buy':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'dont buy':
                bot.send_message(call.message.chat.id, 'Бывает 😢')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True, interval=0)
