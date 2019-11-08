import http_service as hs


__cache = {}


def get_all_pokemon_urls():
    if 'urls' not in __cache:
        print('Fetching all pokemon urls...')
        __cache['urls'] = hs.get_all_urls('pokemon')
    else:
        print('Fetching all pokemon urls from cache...')
    return __cache['urls']


def get_all_pokemon():
    print('Fetching all pokemon')
    return hs.get_resources(get_all_pokemon_urls())


def get_pokemon(name_or_id):
    url = 'https://pokeapi.co/api/v2/pokemon/' + name_or_id
    return hs.get_resource(url)


def get_all_species_urls():
    return hs.get_all_urls('pokemon-species')


def get_all_species():
    print('Fetching all pokemon species')
    return hs.get_resources(get_all_species_urls())


def get_evolution_chain_map():
    print('Generating evolution chain map')
    species = get_all_species()
    return { sp['name'] : sp['evolution_chain']['url'] for sp in species }