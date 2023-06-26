import emoji
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandReminder
from loader import dp


@dp.message_handler(CommandReminder())
@dp.message_handler(commands=["Создать_напоминание" + emoji.emojize(':envelope_with_arrow:')])
async def bot_reminder(message: types.Message):
    await message.answer("В разработке! " + emoji.emojize(':pen:'))
 