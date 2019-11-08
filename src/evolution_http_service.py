import http_service as hs


def get_all_evolution_urls():
    url = 'https://pokeapi.co/api/v2/evolution-chain/?limit=10000'
    results = hs.get_resource(url)['results']
    return list(map(lambda res: res['url'], results))


def get_all_evolution_chains():
    print('Fetching all evolution chains')
    evolution_chains = []
    for url in get_all_evolution_urls():
        evolution_chains.append(hs.get_resource(url))
    return evolution_chains
