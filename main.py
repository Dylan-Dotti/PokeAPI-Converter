import pokemon_http_service as phs
import mongo_service as ms


def convert_pokemon_data():
    print('Downloading pokemon data...')
    pokemon_data = phs.get_all_pokemon()
    print('Download complete. Uploading to database...')
    ms.insert_many(pokemon_data, 'pokeapi', 'pokemon')
    print('Upload complete.')


convert_pokemon_data()
