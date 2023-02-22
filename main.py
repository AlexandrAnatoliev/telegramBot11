# telegramBot11
# Обработка команд /start и /help
# https://www.youtube.com/watch?v=VWjCv_IDuyQ&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=4

# ЗАМЕЧАНИЯ:
# message.reply - ответить на сообщение
# message.answer - послать сообщение
# message.delete - удалить сообщение пользователя из чата

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


if __name__ == '__main__':
    executor.start_polling(dp)
