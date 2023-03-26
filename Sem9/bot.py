from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot_gb = Bot("6021555391:AAECbdsS3oChSgCrQKJVvNbCgWfJ9E6kC0U")
dp =Dispatcher(bot_gb)
async def on_start(_):
    print('Бот запущен')

urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='Питон', url='https://docs.google.com/document/d/1-xynJRDK4z7BfYFJEIVURZrgcEV4agwxIx18XtxkXWo/edit?usp=sharing')
urlButton2 = InlineKeyboardButton(text='Конфликтология', url='https://docs.google.com/document/d/15w1cut1NAUkzY6LP-CRKF9ZzRzynl0OUb751JS2ddMk/edit?usp=sharing')
urlButton3 = InlineKeyboardButton(text='Инициация и планирование проектов', url='https://docs.google.com/document/d/16U-XtLSSwquYFa1Hl-SB-HytjO-vjruKQXZtp69zptM/edit?usp=sharing')
urlButton4 = InlineKeyboardButton(text='Дипломная работа', url='https://docs.google.com/document/d/1FPoKEJDF60jC4WYxPaFkBge6C2qdM308hC0eNnm-zss/edit?usp=sharing')
urlkb.add(urlButton, urlButton2, urlButton3, urlButton4)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Нужна помощь"),
            types.KeyboardButton(text="И так все помню"),

        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)

    await message.answer("Привет!\nЯ помогу тебе освежить знания по учебе в ГБ\n Выбери пункт меню",
                        reply_markup=keyboard)
    print(message)

@dp.message_handler()
async  def com_help(message: Message):
    if message.text == "Нужна помощь":

         await message.answer(
            f'{message.from_user.first_name}, я помогу тебе подобрать информацию по предметам')
         await message.answer('выбери предмет:', reply_markup=urlkb)
    elif message.text == 'И так все помню':
        await message.answer(f'{message.from_user.first_name}, молодец, горжусь тобой))')
    print(message)



executor.start_polling(dp, skip_updates=True, on_startup=on_start)
