import requests
import os
from uploade_url import uploade_url


def get_url_photo_spacex(folder_names):
    url = "https://api.spacexdata.com/v5/launches/"
    response = requests.get(url)
    for link_photo_spacex in response.json():
        if link_photo_spacex["links"]["flickr"]["original"]:
            photos_url = link_photo_spacex["links"]["flickr"]["original"]
    for number, link in enumerate(photos_url):
        filename = f'spacex{number}.jpg'
        path = os.path.join(folder_names, filename)
        uploade_url(link, path)


def main():
    folder_names = 'images'
    get_url_photo_spacex(folder_names)


if __name__ == '__main__':
    main()
