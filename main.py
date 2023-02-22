# telegramBot11
# Обработка команд /start и /help, /description, которая будет выводить описание бота.
# Бот отвечает на сообщение пользователя рандомным символом алфавита.
# https://www.youtube.com/watch?v=VWjCv_IDuyQ&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=4
import random

# ЗАМЕЧАНИЯ:
# message.reply - ответить на сообщение
# message.answer - послать сообщение
# message.delete - удалить сообщение пользователя из чата

# ПРАКТИКА:
# Напишите бота, который будет отвечать на сообщение пользователя рандомным символом алфавита.
# Модифицируйте бота, добавив функцию обработки команды /description, которая будет выводить описание бота

from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_API

HELP_COMMAND = """
/help - список команд
/start - начать работу с ботом
"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def command(message: types.Message):
    await message.answer(text="Добро пожаловать в наш телеграмм-бот")
    await message.delete()


@dp.message_handler(commands='help')
async def command(message: types.Message):
    await message.reply(text=HELP_COMMAND)


@dp.message_handler()  # обрабатываем входящие сообщения
async def echo_upper(message: types.Message):  # объект message класса message
    """
    Бот отвечает на сообщение пользователя рандомным символом алфавита

    :param message: сообщение
    :return: случайная буква из текстового сообщения
    """
    answ = message.text  # сообщение пользователя
    await message.answer(random.choice(answ))  # случайная буква из текстового сообщения


if __name__ == '__main__':
    executor.start_polling(dp)
