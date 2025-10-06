import telebot

token = 'telebot'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Здорова, брат! Я бот.")

@bot.message_handler(commands=['help'])
def handle_start(message):
    bot.send_message(message.chat.id, "Так и быть, я постораюсь тебе помочь")

@bot.message_handler(commands=['command2'])
def handle_start(message):
    bot.send_message(message.chat.id, "Ты молодец" or "Ты лучший")


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
     bot.infinity_polling()
