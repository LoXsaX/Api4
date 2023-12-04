import requests
import os
from uploade_url import uploade_url


def get_url_photo_SpaceX():
    url = "https://api.spacexdata.com/v5/launches/"
    response = requests.get(url)
    for link_photo_SpaceX in response.json():
        if link_photo_SpaceX["links"]["flickr"]["original"]:
            url_photo = link_photo_SpaceX["links"]["flickr"]["original"]
    return url_photo


def fetch_spacex_last_launch(url_photo, folder_names):
    for number, link in enumerate(url_photo):
        filename = f'SpaceX{number}.jpg'
        path = os.path.join(folder_names, filename)
        uploade_url(link, path)


def main():
    get_url_photo_SpaceX()


if __name__ == '__main__':
    main()
