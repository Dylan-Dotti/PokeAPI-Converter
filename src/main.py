
if __name__ == '__main__':
    import sys
    import pokemon_http_service as ps
    import pokemon_species_http_service as pss
    import evolution_chain_http_service as es
    import mongo_service as ms


    def convert_pokemon_data(pokemon_service, species_service):
        print('Downloading pokemon data...')
        pokemon_data = pokemon_service.get_all()
        # merge evolution_chain data from pokemon species
        print('Download complete. Uploading to database...')
        ms.insert_many(pokemon_data, 'pokemon')
        print('Upload complete.')


    def convert_evolution_data(evo_service):
        print('Downloading evolution chain data...')
        evolution_data = evo_service.get_all_evolution_chains()
        print('Download complete. Uploading to database...')
        ms.insert_many(evolution_data, 'evolution-chains')
        print('Upload complete.')


    pokemon_service = ps.PokemonHttpService()
    pokemon_species_service = pss.PokemonSpeciesHttpService()
    evolution_service = es.EvolutionChainHttpService()
    
    for i in range(1, len(sys.argv)):
        command = sys.argv[i]
        if command == 'pokemon':
            convert_pokemon_data(pokemon_service, pokemon_species_service)
        elif command == 'evolution_chains':
            convert_evolution_data(evolution_service)
