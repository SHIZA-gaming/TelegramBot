import telebot
import const
import os
import urllib.request as urllib2
from telebot import types

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
    bot.send_message(message.chat.id, "Мы закончили?... Ладно...(", reply_markup=remove_markup)
#Убрать клавиаткуру

@bot.message_handler(commands=["help"])
def heandle_help(message):
    bot.send_message(message.chat.id, """Мои возможности весьма спецефичны, но, ты тоько псомотри!
    Всё работает!!!""")
#Команда /help

@bot.message_handler(content_types=['text'])
def heandle_text(message):
    if message.text == "IPhone 12":
        # url = "https://drive.google.com/file/d/1dIyX758WYc7EL64wO13DZCrVDoyCcss0/view?usp=sharing"
        # urllib2.urlretrieve(url, "url_image.jpg")
        #open(directory + "IP12.jfif", 'rb')
        IP12img = "https://drive.google.com/file/d/1dIyX758WYc7EL64wO13DZCrVDoyCcss0/view?usp=sharing"
        IP12text = "IPhone 12 есть в 5 цветах: Black(осуждаю!), White, Green, Blue, (PRODUCT) Red.\n Купи IPhone 12 всего лишь за 80.000 рублей" 

        markup = types.InlineKeyboardMarkup(row_width=2) 
        option1_12 = types.InlineKeyboardButton("Купить", callback_data='buy_12_12mini')
        option2_12 = types.InlineKeyboardButton("Не покупать", callback_data='dont_buy')
        markup.add(option1_12, option2_12)

        bot.send_photo(message.from_user.id, IP12img)
        bot.send_message(message.chat.id, IP12text, reply_markup=markup)
        
    elif message.text == "IPhone 12 mini":
        #directory = "https://drive.google.com/drive/folders/1t7IfUcHYp4AhTjOcKgG499ul7cp09ZNu?usp=sharing"
        #open(directory + "mini.jpeg", 'rb')
        IP12MINIimg = "https://drive.google.com/file/d/1k1wqU6Q7pU-cMm76mT0Y3KYS1U1Ogf7P/view?usp=sharing"
        IP12MINItext = "IPhone 12 mini есть в 5 цветах: Black(осуждаю!), White, Green, Blue, (PRODUCT) Red.\n Купи IPhone 12 mini всего за какие-то жалкие 70.000 рублей!"

        markup = types.InlineKeyboardMarkup(row_width=2) 
        option1_12_mini = types.InlineKeyboardButton("Купить", callback_data='buy_12_12mini')
        option2_12_mini = types.InlineKeyboardButton("Не покупать", callback_data='dont_buy')
        markup.add(option1_12_mini, option2_12_mini)

        bot.send_photo(message.from_user.id, IP12MINIimg)
        bot.send_message(message.chat.id, IP12MINItext, reply_markup=markup)

    elif message.text == "IPhone 12 Pro":
        # directory = "https://drive.google.com/drive/folders/1t7IfUcHYp4AhTjOcKgG499ul7cp09ZNu?usp=sharing"
        # open(directory + "IP12PRO.jfif", 'rb')
        IP12PROimg = "https://drive.google.com/file/d/1dcINWcJzzOgV-xnnn1KFFcWQylFQ6K5R/view?usp=sharing"
        IP12PROtext = "IPhone 12 Pro есть в 4 цветах: Graphite, Silver, Gold, Pacific Blue\n Купи IPhone 12 Pro всего за 100.000 рублей!"

        markup = types.InlineKeyboardMarkup(row_width=2) 
        option1_12_pro = types.InlineKeyboardButton("Купить", callback_data='buy_12pro_proMax')
        option2_12_pro = types.InlineKeyboardButton("Не покупать", callback_data='dont_buy')
        markup.add(option1_12_pro, option2_12_pro)

        bot.send_photo(message.from_user.id, IP12PROimg)
        bot.send_message(message.chat.id, IP12PROtext, reply_markup=markup)

    elif message.text == "IPhone 12 Pro Max" :
        # directory = "C:/Users/g.chistopolskij/github/TelegramBot/photo"
        # open(directory + "IP12PROMAX.jpg", 'rb')
        IP12PROMAXimg = "https://drive.google.com/file/d/1DFpzujWpGjliN3hrmRsLK5-htJ6Nt5cl/view?usp=sharing"
        IP12PROMAXtext = "IPhone 12 Pro Max есть в 4 цветах: Graphite, Silver, Gold, Pacific Blue\n Купи IPhone 12 Pro Max всего за 110.000 рублей!"

        markup = types.InlineKeyboardMarkup(row_width=2) 
        option1_12_proMax = types.InlineKeyboardButton("Купить", callback_data='buy_12pro_proMax')
        option2_12_proMax = types.InlineKeyboardButton("Не покупать", callback_data='dont_buy')
        markup.add(option1_12_proMax, option2_12_proMax)

        bot.send_photo(message.from_user.id, IP12PROMAXimg)
        bot.send_message(message.chat.id, IP12PROMAXtext, reply_markup=markup)

    elif message.text == "IPhone 11" :
        # directory = "C:/Users/g.chistopolskij/github/TelegramBot/photo"
        # open(directory + "IP11.jfif", 'rb')
        IP11img = "https://drive.google.com/file/d/1KcIoYZW5dD4LgDx_JWhoLJ7YTdtXUgNA/view?usp=sharing"
        IP11text = "IPhone 11 есть в 6 цветах: White, Black(осуждаю!), Green, Yellow, Purple, (PRODUCT)Red\n Купи IPhone 11 всего за 55.000 рублей!"

        markup = types.InlineKeyboardMarkup(row_width=2) 
        option1_11 = types.InlineKeyboardButton("Купить", callback_data='buy_11')
        option2_11 = types.InlineKeyboardButton("Не покупать", callback_data='dont_buy')
        markup.add(option1_11, option2_11)

        bot.send_photo(message.from_user.id, IP11img)
        bot.send_message(message.chat.id, IP11text, reply_markup=markup)

    elif message.text == "IPhone 11 Pro" :
        IP11PROimg = "https://drive.google.com/file/d/1d8R0mpRJ4ICwLSCWk3bFGACTO8O3aUrc/view?usp=sharing"
        IP11PROtext = "IPhone 11 Pro есть в 4 цветах: Dark green, Silver, Space Grey, Gold.\n Купи IPhone 11 Pro всего за 80.000 рублей !"
        
        markup = types.InlineKeyboardMarkup(row_width=2) 
        option1_11pro = types.InlineKeyboardButton("Купить", callback_data='buy_11pro')
        option2_11pro = types.InlineKeyboardButton("Не покупать", callback_data='dont_buy')
        markup.add(option1_11pro, option2_11pro)

        bot.send_photo(message.from_user.id, IP11PROimg)
        bot.send_message(message.chat.id, IP11PROtext, parse_mode='Markdown', reply_markup=markup)
        

    elif message.text == "IPhone 11 Pro Max" : 
        IP11PROMAXimg  = "https://drive.google.com/file/d/1xJixu2NOBoPhNa6fR1otA5Vig7Me3jse/view?usp=sharing"
        IP11PROMAXtext = "IPhone 11 Pro Max есть в 4 цветах: Dark green, Silver, Space Grey, Gold.\n Купи IPhone 11 Pro Max всего за 90.000 рублей !"

        markup = types.InlineKeyboardMarkup(row_width=2) 
        option1_11proMax = types.InlineKeyboardButton("Купить", callback_data='buy_11proMax')
        option2_11proMax = types.InlineKeyboardButton("Не покупать", callback_data='dont_buy')
        markup.add(option1_11proMax, option2_11proMax)

        bot.send_photo(message.from_user.id, IP11PROMAXimg)
        bot.send_message(message.chat.id, IP11PROMAXtext, parse_mode='Markdown', reply_markup=markup)

    
    elif message.text == "IPhone XS Max" :
        IPXSMAXimg = "https://drive.google.com/file/d/14fn5nxVCdMkOHferGt3pm5YVy_Mo7qg2/view?usp=sharing"
        IPXSMAXtext = "IPhone XS Max есть в 3 цветах: Space Gray, Silver, Gold.\n Купить IPhone XS Max всего за 65.000 рублей !"

        markup = types.InlineKeyboardMarkup(row_width=2) 
        option1_XSMax = types.InlineKeyboardButton("Купить", callback_data='buy_11proMax')
        option2_XSMax = types.InlineKeyboardButton("Не покупать", callback_data='dont_buy')
        markup.add(option1_XSMax, option2_XSMax)

        bot.send_photo(message.from_user.id, IPXSMAXimg)
        bot.send_message(message.chat.id, IPXSMAXtext, parse_mode='Markdown', reply_markup=markup)



            # img.close()
        # bot.send_message(message.chat.id, f'{IP12img}\n{IP12text}')
#elif message.text == "IPhone 11"
        # bot.send_message(message.chat.id, f'{IP12img}\n{IP12text}')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'buy_12_12mini':
                bot.send_message(call.message.chat.id, 'https://www.apple.com/ru/shop/buy-iphone/iphone-12 😊')
            elif call.data == 'buy_12pro_proMax':   
                bot.send_message(call.message.chat.id, 'https://www.apple.com/ru/shop/buy-iphone/iphone-12-pro')
            elif call.data == 'buy_11':
                 bot.send_message(call.message.chat.id, "https://www.apple.com/ru/shop/buy-iphone/iphone-11")
            elif call.data == 'buy_11pro':
                bot.send_message(call.message.chat.id, 'https://www.svyaznoy.ru/catalog/phone/224/5633201')
            elif call.data == "buy_11proMax":
                bot.send_message(call.message.chat.id, "https://shop.mts.ru/catalog/smartfony/apple/iphone-11-pro-iphone-11-pro-max/")
            elif call.data == 'dont_buy':
                bot.send_message(call.message.chat.id, 'Бывает 😢')

            # remove inline buttons
            # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Ты точено этого хочешь?",
            #     reply_markup=None)

             # show alert
            #  bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            #      text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True, interval=0)
