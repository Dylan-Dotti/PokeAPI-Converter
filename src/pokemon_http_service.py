import http_service as hs


class PokemonHttpService(hs.HttpService):
    def __init__(self):
        super().__init__('pokemon')


#def get_evolution_chain_map():
 #   print('Generating evolution chain map')
  #  species = get_all_species()
   # return { sp['name'] : sp['evolution_chain']['url'] for sp in species }