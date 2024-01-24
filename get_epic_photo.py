import requests
import os
from uploade_url import uploade_url
import datetime
from dotenv import load_dotenv


def get_epic_photos(folder_name, api_key):
    url = "https://api.nasa.gov/EPIC/api/natural/image"
    count = 5
    params = {'api_key': api_key, 'count': count}
    response = requests.get(url, params=params)
    response.raise_for_status()
    for image_epic in response.json():
        epic_name = image_epic['image']
        epic_date = image_epic['date']
        epic_time = datetime.datetime.fromisoformat(epic_date).strftime(
            "%Y/%m/%d")
        epic_link = f'https://api.nasa.gov/EPIC/archive/natural//{epic_time}/png/{epic_name}.png'
        path = os.path.join(folder_name, f'{epic_name}.png')
        uploade_url(epic_link, path, params)


def main():
    load_dotenv()
    api_key = os.environ['NASA_KEY']
    folder_name = 'images' 
    get_epic_photos(folder_name, api_key)


if __name__ == '__main__':  
    main()
