import telebot
import const

bot = telebot.TeleBot(const.token)

bot.send_message(1112519987, "test")

upd = bot.get_updates()
print(upd)

last_upd = upd[-1]
message_from_user = last_upd.message
print(message_from_user)
print(bot.get_me())

a  =42
b = "gdjngknghk"

print(type(a), type(b))

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
    user_markup.row("/start", "/stop", "help")
    user_markup.row(u'\u263A')
    user_markup.row("фото", "аудио", "документы",)
    user_markup.row("стикер", "видео", "голос", "локация")
    bot.send_message(message.chat.id,  "Добро пожаловать..", reply_markup=user_markup)


@bot.message_handler(commands=["stop"])
def heandle_stop(message):
    remove_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,  "...", reply_markup=remove_markup)


@bot.message_handler(commands=["help"])
def heandle_help(message):
    bot.send_message(message.chat.id, """Мои возможности весьма спецефичны, но, ты тоько псомотри!
Всё работает!!!""")


@bot.message_handler(content_types=['text'])
def heandle_text(message):
    answer = "Loh"
    if message.text == 'фото':
        directory = "C:/Users/Zerg/PycharmProjects/Telegrambot/photo"

        all_files_in_directory = os.listdir(directory)
        bot.send_chat_action(message.chat.id, "upload_phohto")
        bot.send_photo(message.chat.id, const.template_photo_id)

    if message.text == 'a':
        answer = "B"
        log(message, answer)
        bot.send_message(message.chat.id, "B")
    elif message.text == "c":
        answer = "C"
        log(message, answer)
        bot.send_message(message.chat.id, "C")
    elif message.text == "1" or message.text == "2":
        bot.send_message(message.chat.id, "Либо 1 либо 2....")
    elif message.text == "?" and str(message.from_user.id) == "1112519987":
        bot.send_message(message.chat.id, "Ты избранный!")
    else:
        bot.send_message(message.chat.id, answer)
        log(message, answer)


bot.polling(none_stop=True, interval=0)
