import emoji
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandCancel
from loader import dp


@dp.message_handler(CommandCancel())
async def bot_pogoda(message: types.Message):
    await message.answer("Что-бы там ни было - отменено " + emoji.emojize(':upside-down_face:'))