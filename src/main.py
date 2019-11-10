
if __name__ == '__main__':
    import sys
    import pokemon_http_service as ps
    import pokemon_species_http_service as pss
    import evolution_chain_http_service as es
    import mongo_service as ms

    def convert_pokemon_data(pokemon_service, species_service):
        print('Dropping existing pokemon data')
        ms.drop_collection('pokemon')
        print('Downloading pokemon data...')
        pokemon_data = pokemon_service.get_all()
        print('Download complete. Uploading to database...')
        ms.insert_many(pokemon_data, 'pokemon')
        print('Transfer complete.')

    def convert_species_data(species_service):
        print('Dropping existing species data')
        ms.drop_collection('pokemon-species')
        print('Downloading species data...')
        species_data = species_service.get_all()
        print('Download complete. Uploading to database...')
        ms.insert_many(species_data, 'pokemon-species')
        print('Transfer complete.')

    def convert_evolution_data(evo_service):
        print('Dropping existing evolution data')
        ms.drop_collection('evolution-chain')
        print('Downloading evolution chain data...')
        evo_data = evo_service.get_all()
        print('Download complete. Uploading to database...')
        ms.insert_many(evo_data, 'pokemon-species')
        print('Transfer complete.')


    pokemon_service = ps.PokemonHttpService()
    pokemon_species_service = pss.PokemonSpeciesHttpService()
    evolution_service = es.EvolutionChainHttpService()
    
    for i in range(1, len(sys.argv)):
        command = sys.argv[i]
        if command == 'pokemon':
            convert_pokemon_data(pokemon_service, pokemon_species_service)
        elif command == 'pokemon_species':
            convert_species_data(pokemon_species_service)
        elif command == 'evolution_chain':
            convert_evolution_data(evolution_service)
