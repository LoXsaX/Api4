import requests
import os
from uploade_url import uploade_url


def get_url_photo_spacex():
    url = "https://api.spacexdata.com/v5/launches/"
    response = requests.get(url)
    for link_photo_spacex in response.json():
        if link_photo_spacex["links"]["flickr"]["original"]:
            photos_url = link_photo_spacex["links"]["flickr"]["original"]
    return photos_url


def fetch_spacex_last_launch(photos_url, folder_names):
    for number, link in enumerate(photos_url):
        filename = f'spacex{number}.jpg'
        path = os.path.join(folder_names, filename)
        uploade_url(link, path)


def main():
    get_url_photo_spacex()


if __name__ == '__main__':
    main()
