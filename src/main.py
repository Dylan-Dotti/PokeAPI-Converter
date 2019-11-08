
if __name__ == '__main__':
    import sys
    import pokemon_http_service as phs
    import evolution_http_service as ehs
    import mongo_service as ms


    def convert_pokemon_data():
        print('Downloading pokemon data...')
        pokemon_data = phs.get_all_pokemon()
        print('Download complete. Uploading to database...')
        ms.insert_many(pokemon_data, 'pokeapi', 'pokemon')
        print('Upload complete.')


    def convert_evolution_data():
        print('Downloading evolution chain data...')
        evolution_data = ehs.get_all_evolution_chains()
        print('Download complete. Uploading to database...')
        ms.insert_many(evolution_data, 'pokeapi', 'evolution-chains')
        print('Upload complete.')

    phs.get_all_pokemon_urls()
    phs.get_all_pokemon_urls()
    for i in range(1, len(sys.argv)):
        command = sys.argv[i]
        if command == 'pokemon':
            convert_pokemon_data()
        elif command == 'evolution_chains':
            convert_evolution_data()
