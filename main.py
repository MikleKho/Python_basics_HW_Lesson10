import telebot
from buttons import calc_button


bot = telebot.TeleBot('5753200879:AAHJBOLSDW1HaEDc_bJZdYg1CesAXNbu6Nc')
value = ''
start_value = ''

@bot.message_handler(commands=["start"])
def getMessage(message):
    global value
    if value == '':
        bot.send_message(message.from_user.id, "0", reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, start_value
    data = query.data

    if data == "C":
        value = ""

    elif data == "<=":
        if value != '':
            value = value[:len(value)-1]
    elif data == "=":
        try:
            value = str(eval(value))
        except:
            value = "Error"

    else:
        value += data

    if (value != start_value and value != '') or ('0' != start_value and value == ''):
        if value == '':
            bot.edit_message_text(chat_id=query.message.chat.id,
                                  message_id=query.message.id, text="0", reply_markup=keyboard)
            start_value = "0"
        else:
            bot.edit_message_text(chat_id=query.message.chat.id,
                                  message_id=query.message.id, text=value, reply_markup=keyboard)
            start_value = value

    if value == "Error":
        value = ''


@bot.message_handler(content_types=["text"])
def mess(message):
    mess = f'{message.from_user.first_name}, ---> "/start" to begin. Click buttons only'
    bot.send_message(message.chat.id, mess)

print("Bot started. '/start' to begin")
keyboard = calc_button()

bot.polling(none_stop=False, interval=0)
