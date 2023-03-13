import telebot 
import openai

bot=telebot.TeleBot('Token_ID')  # find a @BotFather -- > /newbot


@bot.message_handler(commands=['s'],content_types=['text']) #command call
def handle_text(message):
    response = openai.Completion.create(
        engine='text-davinci-003',   #Davinci - 003 DataBase (2021)
        prompt=f"{message.text}",
        max_tokens=1024,   #limit of letters , we also can up it to 5000
        n=5, 
        stop=None,
        temperature=0.5, ) 
    bot.send_message(message.chat.id, response.choices[0].text)

bot.polling()