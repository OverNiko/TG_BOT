import emoji
from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Начать диалог " + emoji.emojize(':right_arrow:')),
            types.BotCommand("cancel", "Отменить действие " + emoji.emojize(':cross_mark:')),
            types.BotCommand("help", "Вывести справку " + emoji.emojize(':bookmark_tabs:')),
            # types.BotCommand("pogoda", "Узнать погоду " + emoji.emojize(':sun:')),
            # types.BotCommand("reminder", "Создать напоминание " + emoji.emojize(':envelope_with_arrow:')),
        ]
    )
