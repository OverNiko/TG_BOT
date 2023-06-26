import emoji
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог " + emoji.emojize(':right_arrow:'),
            "/cancel - Отменить действие " + emoji.emojize(':cross_mark:'),
            "/help - Вывести справку " + emoji.emojize(':bookmark_tabs:'),
            "/pogoda - Узнать погоду " + emoji.emojize(':sun:'),
            "/reminder - создать напоминание " + emoji.emojize(':envelope_with_arrow:'),
            )
    
    await message.answer("\n".join(text))
