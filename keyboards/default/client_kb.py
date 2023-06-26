import emoji
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b1 = KeyboardButton("/Узнать_погоду" + emoji.emojize(':sun:'))
b2 = KeyboardButton("/Создать_напоминание" + emoji.emojize(':envelope_with_arrow:'))

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2)