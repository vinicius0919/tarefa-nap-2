#CLASSE PROPRIEDADE: DESENVILVIDA EM SALA DE AULA
#UTILIZADA EM CONJUNTO COM AS CLASSES BOI E CRUD
class Propriedade:
    def __init__(self, nome, endereco, cnpj):
        self._id = None
        self._nome = nome
        self._endereco = endereco
        self._cnpj = cnpj

    @classmethod
    def construtor_alternativo(cls,id, nome, endereco, cnpj):
        propriedade = cls(nome, endereco, cnpj)
        propriedade._id = id
        return propriedade
    
    # Métodos Get
    def get_info(self):
        return [self._id, self._nome, self._endereco, self._cnpj]

    def get_id(self):
        return self._id

    def get_nome(self):
        return self._nome

    def get_endereco(self):
        return self._endereco

    def get_cnpj(self):
        return self._cnpj

    # Métodos Set
    def set_id(self, novo_id):
        self._id = novo_id

    def set_proprietario(self, newName):
        self._nome = newName

    def set_endereco(self, novo_endereco):
        self._endereco = novo_endereco

    def set_cnpj(self, novo_cnpj):
        self._cnpj = novo_cnpj
