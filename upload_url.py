import requests

def upload_url(url, path, params=None):
    response = requests.get(url, params)
    response.raise_for_status()
    
    with open(path, 'wb') as file:
        file.write(response.content)
