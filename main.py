import telebot
import const

bot = telebot.TeleBot(const.token)


upd = bot.get_updates()
print(upd)

last_upd = upd[-1]
message_from_user = last_upd.message
print(message_from_user)
print(bot.get_me())


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
    user_markup.row("IPhone 12", "IPhone 11", "IPhone 10")
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
    img = "https: // imbt.ga / H2EykWkfnH"
    text = "IPhone 12 - ещё нет в продаже на оффициальном сайте ЭППЛ,но зато есть у нас." \
           " IPhone 12 есть в 3 цветах: Purple, White, Black" \
           " Купи IPhone 12 всего лишь за 120,000 рублей"
    if message.text == "IPhone 12":
        bot.send_message(message.chat.id, f'{img}\n{text}')


bot.polling(none_stop=True, interval=0)
