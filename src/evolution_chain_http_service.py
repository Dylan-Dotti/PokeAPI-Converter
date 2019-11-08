import http_service as hs

class EvolutionChainHttpService(hs.HttpService):
    def __init__(self):
        super().__init__('evolution-chain')
