import requests
import os
from urllib.parse import unquote, urlparse
from uploade_url import uploade_url
from dotenv import load_dotenv


def get_filename(link):
    decoder_link = unquote(link)
    parsed_link = urlparse(decoder_link)
    path, name = os.path.split(parsed_link.path)
    file_extention_path = os.path.splitext(name)
    filename, extention = file_extention_path
    return extention, filename


def fetch_nasa_apod(folder_names, api_key):
    url = "https://api.nasa.gov/planetary/apod"
    params = {'api_key': api_key, 'count': 30}
    response = requests.get(url, params=params)
    response.raise_for_status()
    for image_apod in response.json():
        if image_apod.get('media_type') == 'image':
            if image_apod.get('hdurl'):
                apod_link_image = image_apod['hdurl']
            else:
                apod_link_image = image_apod['url']
            extention, filename = get_filename(apod_link_image)
            path = os.path.join(folder_names, f'{filename}{extention}')
            uploade_url(apod_link_image, path)


def main():
    load_dotenv()
    api_key = os.environ['NASA_KEY']
    folder_names = 'images'
    fetch_nasa_apod(folder_names, api_key)


if __name__ == '__main__':
    main()
