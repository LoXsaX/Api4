import requests
import os
from upload_url import upload_url


def get_url_photo_spacex(folder_name):
    url = "https://api.spacexdata.com/v5/launches/"
    response = requests.get(url)
    response.raise_for_status()
    for link_photo_spacex in response.json():
        if link_photo_spacex["links"]["flickr"]["original"]:
            photo_urls = link_photo_spacex["links"]["flickr"]["original"]
    for number, link in enumerate(photo_urls):
        filename = f'spacex{number}.jpg'
        path = os.path.join(folder_name, filename)
        upload_url(link, path)


def main():
    folder_name = 'images'
    get_url_photo_spacex(folder_name)


if __name__ == '__main__':
    main()
