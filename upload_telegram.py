import requests
from pathlib import Path
import os
from os import listdir
import datetime
from time import sleep
import telegram
import random
from dotenv import load_dotenv


def upload_auto(tg_token, chat_id):
    bot = telegram.Bot(token=tg_token)
    folder = 'images'
    files = listdir(folder)
    sleep = 14400
    random.shuffle(files)
    for file in files:
        file_path = os.path.join(folder, file)
        with open(file_path, 'rb') as f:
            bot.send_document(chat_id, document=f)
        sleep


def main():
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    chat_id= os.environ['CHAT_ID']
    folder_names = 'images'
    Path(folder_names).mkdir(parents=True, exist_ok=True)
    upload_auto(tg_token, chat_id)


if __name__ == '__main__':
    main()

