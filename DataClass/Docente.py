class Docente:

    def __init__(self, siape, nome):
    
        self.siape = siape
        self.nome = nome

    def getDocente_JSON (self):

        saida = "{\"SIAPE\":'"+self.siape+"', \"Nome\":'"+self.nome+"'}"
        return saida