import os
import time
import random
import asyncio
from telegram import Bot

PHOTO = '/path'
TEXT = '/path'
TOKEN = 'xxxxxxxxxxxx-xxxxxxxxxx-999'

bot = Bot(token=TOKEN)

photo = os.listdir(PHOTO)
text = os.listdir(TEXT)
 
used_photo = []
used_text = []

# def random_files(directory):
#    files = os.listdir(directory)
#    random_file = random.choice(files)
#    file_path = os.path.join(directory, random_file)
#    return file_path 

def unused(file_list, used_list): 
    unused_list = list(set(file_list) - set(used_list)) 
    return unused_list 

def random_photo_path(photo, used_photo): 
    if len(used_photo) == len(photo):
        used_photo.clear() 
    unused_photo = unused(photo, used_photo)
    random_photo = random.choice(unused_photo) 
    used_photo.append(random_photo) 
    photo_path = os.path.join(PHOTO, random_photo)
    return photo_path

def random_text_path(text, used_text): 
    if len(used_text) == len(text): 
        used_text.clear() 
    unused_text = unused(text, used_text) 
    random_text = random.choice(unused_text) 
    used_text.append(random_text) 
    text_path = os.path.join(TEXT, random_text) 
    return text_path 

async def send(text, photo):
    photo_path_file = random_photo_path(photo, used_photo) 
    text_path_file = random_text_path(text, used_text)
    with open(photo_path_file, 'rb') as photo_file, open(text_path_file, 'r') as text_file:
        await bot.send_photo(chat_id='@testbottelegramapi', photo=photo_file, caption=text_file.read())

async def auto(): 
    while True: 
        await send(text, photo)
        await asyncio.sleep(5) # задержка вывода в секундах

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
