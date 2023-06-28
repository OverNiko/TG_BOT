import emoji
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from loader import dp
from pyowm import OWM
from pyowm.utils.config import get_default_config


class Form(StatesGroup):
    gorod = State()

@dp.message_handler(commands="pogoda")
@dp.message_handler(commands=["Узнать_погоду" + emoji.emojize(':sun:')])
async def bot_pogoda(message: types.Message):
    await Form.gorod.set()
    await message.answer("В  каком вы городе/стране? " + emoji.emojize(':cityscape:'))


@dp.message_handler(state=Form.gorod)
async def process_gorod(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gorod'] = message.text
        
        try:
            place = data['gorod']
            
            if place == "/cancel":
                await state.finish()
                await message.answer(f"Ок " + emoji.emojize(':OK_hand:'))
            
            else:
                config_dict = get_default_config()
                config_dict['language'] = 'ru'

                owm = OWM('a99967bc9ee70d5b4bd387902982f400', config_dict)

                mrg = owm.weather_manager()
                observation = mrg.weather_at_place(place)
                w = observation.weather

                # Температура
                temp = w.temperature('celsius')
                t1 = temp["temp"]
                t2 = temp["feels_like"]
                t3 = temp["temp_max"]
                t3 = temp["temp_min"]
                # Скорость ветра
                wi = w.wind()['speed']
                # Влажность
                humi = w.humidity
                # Облачность
                cl = w.clouds
                # Статус
                st = w.status
                # Детали
                dt = w.detailed_status
                # Время
                ti = w.reference_time('iso')
                # Давление
                pr = w.pressure['press']
                # Видимость
                vd = w.visibility_distance

                text = (f"В городе/стране - {place}, сейчас: {t1}°С , ощущается как {t2}°С",
                        f"Скорость ветра: {wi} м/с " + emoji.emojize(':wind_face:'),
                        f"Влажность: {humi}% " + emoji.emojize(':droplet:'),
                        f"Облачность: {cl}% " + emoji.emojize(':cloud:'),
                        f"Детали: {dt} " + emoji.emojize(':gear:'),
                        f"Справочное время: {ti} " + emoji.emojize(':alarm_clock:'),
                        f"Давление: {pr} мм.ртут.столба " + emoji.emojize(':thermometer:'),
                        f"Видимость: {vd}м " + emoji.emojize(':eyes:'))
                
                await message.answer("\n".join(text))
            
        except:
            await message.answer(f"Такой город\страна - {data['gorod']}, не найден или не существует!!\nВведите корректный город\страну, для отмены введите /cancel")
            process_gorod()
            
    await state.finish()