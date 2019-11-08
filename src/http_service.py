import requests


def get_resource(url):
    print('Fetching resource: ' + url)
    data = requests.get(url=url)
    return data.json()


def get_resources(urls):
    resources = []
    for url in urls():
        resources.append(get_resource(url))
    return resources


def get_all_urls(category):
    url = 'https://pokeapi.co/api/v2/' + category + '?limit=10000'
    results = get_resource(url)['results']
    return list(map(lambda res: res['url'], results))