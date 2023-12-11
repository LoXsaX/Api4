import requests
from pathlib import Path
import os
from os import listdir
import datetime
from fetch_NASA_apod import fetch_NASA_apod
from get_epic_photo import get_epic_photo
from space_X import fetch_spacex_last_launch, request_api_SpaceX
from time import sleep
import telegram
import random
from dotenv import load_dotenv


def loading_auto(tg_token, chat_id):
    bot = telegram.Bot(token=tg_token)
    folder = 'images'
    files = listdir(folder)
    random.shuffle(files)
    for file in files:
        file_path = os.path.join(folder, file)
        with open(file_path, 'rb') as f:
            bot.send_document(chat_id, document=f)
        sleep(10)


def main():
    load_dotenv()
    nasa_key = os.environ['NASA_KEY']
    tg_token = os.environ['TG_TOKEN']
    chat_id= os.environ['CHAT_ID']
    folder_names = 'images'
    Path(folder_names).mkdir(parents=True, exist_ok=True)
    url_photo = request_api_SpaceX()
    get_epic_photo(folder_names, nasa_key)
    fetch_NASA_apod(folder_names, nasa_key)
    fetch_spacex_last_launch(url_photo, folder_names)
    loading_auto(tg_token, chat_id)


if __name__ == '__main__':
    main()

