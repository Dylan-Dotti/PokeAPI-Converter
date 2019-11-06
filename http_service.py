import requests


def get_resource(url):
    print('Fetching resource: ' + url)
    data = requests.get(url=url)
    return data.json()
