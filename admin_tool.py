from aiogram import Bot,Dispatcher, executor,types
from aiogram.dispatcher.storage import FSMContext
import openai
import asyncio
from aiogram.types.input_file import InputFile
from aiogram.utils import executor
from aiogram.utils.exceptions import BotBlocked, ChatNotFound, RetryAfter, TelegramAPIError


proxi = "proxy"
bot=Bot(token="TOKEN_API", proxy=proxi)
dp = Dispatcher(bot)
openai.api_key = "open_ai_key"


@dp.message_handler(commands=['s'])
async def ai_response(message: types.Message):
    prompt = message.text.split('/s')[1]
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text
    await message.reply(response)

@dp.message_handler(commands=["paleski"])
async def forward_message(message: types.Message):
    # Define the chat ID of the user or group to which you want to forward the message

    # Define the chat ID of the Telegram channel from which you want to forward the message
    channel_id = #channel_id

    # Define the message ID of the message you want to forward
    message_id = #message_id

    # Use the forward_message method to forward the message to the user or group
    try:
        await bot.forward_message(chat_id=message.chat.id, from_chat_id=channel_id, message_id=message_id)
    except BotBlocked:
        await message.reply("This bot is blocked by the user.")
    except ChatNotFound:
        await message.reply("The chat_id is invalid.")
    except RetryAfter as e:
        await message.reply(f"Too many requests. Retry after {e.timeout} seconds.")
    except TelegramAPIError:
        await message.reply("An error occurred while forwarding the message.")





words=[...]

@dp.message_handler(content_types=['new_chat_members'])
async def echo(message: types.Message):
    user_name = message.new_chat_members[0].first_name
    await bot.send_message(message.chat.id, f"rules")
@dp.message_handler(commands=['rules'])
@dp.message_handler(commands=['rules_2'])
async def rules(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,text='1....,n')

@dp.message_handler(commands=['link_1'])
async def slownik(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text = 'link')

@dp.message_handler(commands=['link_2'])
async def slownik(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text = '...text...')

@dp.message_handler(commands=['link_2'])
async def info(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='...')

@dp.message_handler(commands=['link_4'])
async def gwary(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='/text')



@dp.message_handler(commands=['command_n_1'])
async def zmudzit(message: types.Message):
    input_array = message.text.split()[1:] #string
    break_marks = ['!', '.', '?', ';', ':', ',',')','(', ' ,', ' .', ', ','. ']
    ending = 'ing'
    for i in range(len(input_array)):
        word = input_array[i]
        if word[-1] in break_marks:
            input_array[i] = word[:-1] + ending + word[-1]
        else:
            input_array[i] += ending
    output_string = ' '.join(input_array)
    await bot.send_message(chat_id=message.chat.id, text=output_string)






#filter of words

@dp.message_handler(content_types=['text'])
async def filter_one(message: types.Message):
    text=message.text.lower()
    for word in words:
        if word in text:
            await bot.send_message(chat_id=message.chat.id, text=f"{message.from_user.first_name}, bad word")
            await bot.delete_message(chat_id=message.chat.id,message_id=message.message_id)





if __name__=='__main__':
    executor.start_polling(dp)
