import http_service as hs

class PokedexEntryHttpService(hs.HttpService):
    def __init__(self):
        super().__init__('pokemon-species')
    
    def get_one(self, identifier):
        species_data = super().get_one(identifier)
        return species_data

    def get_all(self):
        pass