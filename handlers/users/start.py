import emoji
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import kb_client
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! " + emoji.emojize(':hand_with_fingers_splayed:'), reply_markup=kb_client)
