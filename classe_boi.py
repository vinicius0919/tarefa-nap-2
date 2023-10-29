#CLASSE BOI: DESENVOLVIDA EM SALA DE AULA
#CONTEM OS PRINCIPAIS MÉTODOS GET E SET
#UTILIZADA JUNTAMENTE COM A CLASSE CRUD E PROPRIEDADE
#
class Boi:
    def __init__(self, numero, peso):
        self.numero = numero
        self.peso = peso
    
    def get_identificacao(self):
        return self.numero
    
    def get_peso(self):
        return self.peso
    
    def get_id(self):
        return self.numero
    def set_peso(self, novo_peso):
        self.peso = novo_peso
