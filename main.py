import os # модуль для управления системного администрирования
import time # модуль, позволяющий устанавливать задержки в реальном времени (секундах)
import random # модуль для случайного выбора
import asyncio # модуль асинхронного программирования
from telegram import Bot # модуль из скаченной библиотеки Telegram

PHOTO = '/home/serezha/images' # путь к папке с фото. На Windows может принимать иной вид, можно посмотреть в проводнике
TEXT = '/home/serezha/texts' # путь к папке с текстом. /
TOKEN = '6141726757:AAE_JhmM_GDkdhRa_jGjdsT3NQeoYdeEmro' # токен бота. Смотрим в @BotFather

bot = Bot(token=TOKEN) # инициализация объекта

photo = os.listdir(PHOTO) # список элементов папки с фото
text = os.listdir(TEXT) #
 
used_photo = [] # использованные фото
used_text = [] # использованные текста

# def random_files(directory): # поиск пути случайного файла из выбранной директории (функция общего вида)
#    files = os.listdir(directory) # создание списка из файлов директории
#    random_file = random.choice(files) # выбор случайного файла
#    file_path = os.path.join(directory, random_file) # путь файла в директории
#    return file_path # функция возвращает искомый путь 

def unused(file_list, used_list): # функция, возвращающая список элементов, которые еще не были использованы в текущем цикле
    unused_list = list(set(file_list) - set(used_list)) # разница списка всех элементов и списка использованных 
    return unused_list # возвращаем список доступных для использования элементов

def random_photo_path(photo, used_photo): # функция случайного выбора фотографии
    if len(used_photo) == len(photo): # если все элементы были использованы - завершается цикл и список недоступных файлов обнуляется
        used_photo.clear() # обнуление (очищение)
    unused_photo = unused(photo, used_photo) # сохраняем все доступные файлы
    random_photo = random.choice(unused_photo) # выбираем случайный файл из доступных
    used_photo.append(random_photo) # добавляем файл в использованные
    photo_path = os.path.join(PHOTO, random_photo) # сохраняем путь выбранного файла
    return photo_path # возвращаем путь

# функция полностью повторяет верхнуюю, но предназначена для работы с текстом, а не фото

def random_text_path(text, used_text): #
    if len(used_text) == len(text): #
        used_text.clear() #
    unused_text = unused(text, used_text) #
    random_text = random.choice(unused_text) #
    used_text.append(random_text) #
    text_path = os.path.join(TEXT, random_text) #
    return text_path #

async def send(text, photo): # функция выводa
    photo_path_file = random_photo_path(photo, used_photo) # сохраняем пути случайных файлов (текста/фото) // random_files(PHOTO) 
    text_path_file = random_text_path(text, used_text) # // random_files(TEXT)
    with open(photo_path_file, 'rb') as photo_file, open(text_path_file, 'r') as text_file: # открытие файлов
        await bot.send_photo(chat_id='@testbottelegramapi', photo=photo_file, caption=text_file.read()) # вывод файлов в одном потоке

async def auto(): # бесконечный запуск
    while True: # бесконечный цикл, будет работать всегда для вывода и установки задержки вывода
        await send(text, photo) # вызов функции вывода == вывод
        await asyncio.sleep(5) # интервал между выводом. Указывается в секундах. Например, для 3-х дней это значение будет равно 259200

# постоянная структура с элементами асинхронного программирования

async def main():
    await auto()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
