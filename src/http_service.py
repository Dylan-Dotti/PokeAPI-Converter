import requests


class HttpService:
    
    def __init__(self, category_name):
        self.__cache = {}
        self.category = category_name

    def __get_resource(self, url):
        print('Fetching resource: ' + url)
        data = requests.get(url=url)
        return data.json()

    def __get_resources(self, urls):
        resources = []
        for url in urls():
            resources.append(self.__get_resource(url))
        return resources

    def get_urls(self):
        url = 'https://pokeapi.co/api/v2/' + self.category + '?limit=10000'
        if 'urls' not in self.__cache:
            print('Fetching urls for ' + self.category + '...')
            results = self.__get_resource(url)['results']
            urls = list(map(lambda res: res['url'], results))
            self.__cache['urls'] = urls
        else:
            print('Fetching urls for ' + self.category + ' from cache...')
        return self.__cache['urls']

    def get_one(self, identifier):
        url = 'https://pokeapi.co/api/v2/' + self.category + '/' + identifier
        return self.__get_resource(url)

    def get_all(self):
        print('Fetching all ' + self.category)
        return self.__get_resources(self.get_urls())