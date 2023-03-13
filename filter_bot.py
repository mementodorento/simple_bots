import telebot

bot=telebot.TeleBot('bot_token_id')   #BotFather --> /newbot to take TokenID

@bot.message_handler(commands=['rules'])
@bot.message_handler(commands=['правілы'])
def rools(message):
    bot.send_message(message.chat.id, text='rules')


@bot.message_handler(content_types=['text'])
def filter(message):
    if message.text=='bad_word':
        bot.send_message(chat_id=message.chat.id, text='')
        bot.delete_message(chat_id=message.chat.id, message_id=message.id)
  
bot.polling()