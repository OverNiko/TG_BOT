import emoji
from aiogram import types
from loader import dp


@dp.message_handler(commands="cancel")
async def bot_pogoda(message: types.Message):
    await message.answer("Что-бы там ни было - отменено " + emoji.emojize(':upside-down_face:'))