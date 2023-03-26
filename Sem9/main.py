# path = 'C:\\Users\\anton\\PycharmProjects\\seminar\\Sem9\\text_new.txt'
#
# phone_book = []
#
# def load_file(path: str):
#     file = open(path, 'r')
#     data = file.readlines()
#     return data
# # чтение файла
#
# def save_file(path: str, data: str):
#     file = open(path, 'w')
#     file.write(data)
#     file.close()
# # запись файла
#
# # string = 'some text'
# # string_2 = '\nfrom second'
# # file = open(path, 'a')
# # encoding='UTF-8' не сработала кодировка, ошибка
# # data = file.read() чтение всего содержимого
# # data = file.readline() чтение строки
# # data = file.readlines() чтение всех строк
# # file.write(string_2) запись новой строки
# # file.close() закрыть файл
#
# # new_list = [data]
# # print(data)
#
# my_list = load_file(path)
# for contact in my_list:
#     new_data = contact.split(';')
#     temp = {'name': new_data[0].strip(),
#             'phone': new_data[1].strip(),
#             'comment': new_data[2].strip()}
#     phone_book.append(temp)
#
# print(phone_book)
# # print(phone_book[1].get('name')) вывод на печать отдельного элемента справочника
# phone_book[1]['name'] = 'Cloud'
# print(phone_book)
#
# file_to_save = []
#
# for contact in phone_book:
#     str_list = []
#     for value in contact.values():
#         str_list.append(value)
#     file_to_save.append(';'.join(str_list))
#
# save_file(path, '\n'.join(file_to_save))
#
# data = load_file(path)
# print(data)

from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram.types import Message

bot_gb = Bot("6021555391:AAECbdsS3oChSgCrQKJVvNbCgWfJ9E6kC0U")
dp = Dispatcher(bot_gb)
async def on_start(_):
    print('Бот запущен')

@dp.message_handler(commands=['start'])
async def com_start(message: Message):
    # await message.reply('Бот запущен и готов к работе')
    print(message.from_user.id)


@dp.message_handler()
async def com_start(message: Message):
    if message.text == 'молодец':
        await message.reply(f'Спасибо, {message.from_user.first_name}, '
                             f' ты тоже')
    elif message.text == 'дурак':
        await message.reply(f'на себя посмотри')

executor.start_polling(dp, skip_updates=True, on_startup=on_start)
