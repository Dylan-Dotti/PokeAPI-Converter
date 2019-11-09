import getter_service as gs
import requests
import utilities as util

class HttpService(gs.GetterService):
    def __init__(self, category_name):
        self.__cache = {}
        self.category = category_name

    def __get_resource(self, url):
        if url not in self.__cache:
            #print('Fetching resource: ' + url)
            data = requests.get(url=url)
            self.__cache[url] = data.json()
        #else:
            #print('Fetching resource from cache: ' + url)
        return self.__cache[url]

    def __get_resources(self, urls):
        resources = []
        util.print_progress_bar(0, len(urls))
        for index, url in enumerate(urls):
            resources.append(self.__get_resource(url))
            util.print_progress_bar(index + 1, len(urls), same_line=(index <= len(urls)))
        print('')
        return resources

    def get_urls(self):
        url = 'https://pokeapi.co/api/v2/' + self.category + '/?limit=10000'
        if 'urls' not in self.__cache:
            print('Fetching urls for ' + self.category + '...')
        else:
            print('Fetching urls for ' + self.category + ' from cache...')
        results = self.__get_resource(url)['results']
        return [ res['url'] for res in results ]

    def get_one(self, identifier):
        url = 'https://pokeapi.co/api/v2/' + self.category + '/' + identifier
        return self.__get_resource(url)

    def get_all(self):
        print('Fetching all ' + self.category + '...')
        urls = self.get_urls()
        print('Fetching ' + self.category + ' data...')
        return self.__get_resources(urls)