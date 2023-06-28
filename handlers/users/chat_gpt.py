import openai
import requests

from environs import Env
from loader import dp

from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode

env = Env()
env.read_env()

GPT_API = env.str("GPT_API")

openai.api_key = GPT_API

# Определение состояний для FSM
class GPTConversation(StatesGroup):
    waiting_for_text = State()

# Обработчик команды /gpt
@dp.message_handler(commands=["gpt"])
async def gpt_start(message: types.Message):
    await message.answer("Привет! Я GPT-3. Напиши мне что-нибудь, и я сгенерирую продолжение. Чтобы закончить общение, используй команду /cancel.")
    await GPTConversation.waiting_for_text.set()

# Обработчик текстовых сообщений в состоянии waiting_for_text
@dp.message_handler(state=GPTConversation.waiting_for_text)
async def process_gpt_text(message: types.Message, state: FSMContext):
    if message.text == "/cancel":
        await state.finish()
        await message.reply("Общение с GPT-3 завершено.")
    else:
        # Генерация текста с помощью GPT модели
        try:
            response = openai.Completion.create(
                engine="davinci",
                prompt=message.text,
                max_tokens=100,
                n=1,
                stop=None,
                temperature=0.5,
            )
            generated_text = response.choices[0].text
            await message.reply(generated_text)
        except Exception as e:
            await message.reply("Произошла ошибка при генерации текста, воспользуйтесь функцией позже. Чтобы закончить общение, используй команду /cancel.")
        await GPTConversation.waiting_for_text.set()