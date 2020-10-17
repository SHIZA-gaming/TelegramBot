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


@bot.message_handler(commands=["stop"])
def heandle_stop(message):
    remove_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,  "Мы закончили?... Ладно...(", reply_markup=remove_markup)


@bot.message_handler(commands=["help"])
def heandle_help(message):
    bot.send_message(message.chat.id, """Мои возможности весьма спецефичны, но, ты тоько псомотри!
    Всё работает!!!""")


@bot.message_handler(content_types=['text'])
def heandle_text(message):
    # IP12img = "https://imbt.ga/H2EykWkfnH"
    # IP12text = "IPhone 12 - ещё нет в продаже на оффициальном сайте ЭППЛ,но зато есть у нас." \
    #        " IPhone 12 есть в 3 цветах: Purple, White, Black" \
    #        " Купи IPhone 12 всего лишь за 120,000 рублей"
    if message.text == "IPhone 12":
        directory = "C:/Users/g.chistopolskij/github/TelegramBot/photo/"
        IP12img = open(directory + "IP12.jpg", 'rb')
        IP12text = "IPhone 12 есть в 5 цветах: Black(осуждаю!), White, Green, Blue, (PRODUCT) Red.\nКупи IPhone 12\
        всего лишь за 80.000 рублей"
        IP12MINIimg = open(directory + "mini.jpeg", 'rb')
        IP12MINItext = "IPhone 12 mini есть в 5 цветах: Black(осуждаю!), White, Green, Blue, (PRODUCT) Red.\n Купи IPhone 12 mini\
        всего за какие-то жалкие 70.000 рублей.\n \
        https://www.apple.com/ru/shop/buy-iphone/iphone-12"
        bot.send_photo(message.from_user.id, IP12img)
        bot.send_message(message.chat.id, IP12text)
            # img.close()
        # bot.send_message(message.chat.id, f'{IP12img}\n{IP12text}')
#elif message.text == "IPhone 11"
        # bot.send_message(message.chat.id, f'{IP12img}\n{IP12text}')


bot.polling(none_stop=True, interval=0)
