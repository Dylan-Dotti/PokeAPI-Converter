import http_service as hs


def get_all_pokemon_urls():
    url = 'https://pokeapi.co/api/v2/pokemon/?limit=10000'
    results = hs.get_resource(url)['results']
    return list(map(lambda res: res['url'], results))


def get_all_pokemon():
    print('Fetching all pokemon')
    pokemon = []
    for url in get_all_pokemon_urls():
        pokemon.append(hs.get_resource(url))
    return pokemon


def get_pokemon(name_or_id):
    url = 'https://pokeapi.co/api/v2/pokemon/' + name_or_id
    return hs.get_resource(url)
