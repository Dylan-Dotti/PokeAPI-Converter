import http_service as hs


class PokemonSpeciesHttpService(hs.HttpService):
    def __init__(self):
        super().__init__('pokemon-species')