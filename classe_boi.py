class Boi:
    def __init__(self, peso, idPropriedade):
        self.numero = None
        self.peso = peso
        self.idPropriedade = idPropriedade

    @classmethod
    def construtor_alternativo(cls, numero, peso, idPropriedade):
        boi = cls(peso, idPropriedade)
        boi.numero = numero
        return boi

    # Métodos GET
    def get_info(self):
        return  [self.numero, self.peso, self.idPropriedade]
    
    def get_numero(self):
        return self.numero

    def get_peso(self):
        return self.peso

    def get_idPropriedade(self):
        return self.idPropriedade

    # Métodos SET
    def set_numero(self, numero):
        self.numero = numero

    def set_peso(self, peso):
        self.peso = peso

    def set_idPropriedade(self, idPropriedade):
        self.idPropriedade = idPropriedade
