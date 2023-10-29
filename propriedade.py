#CLASSE PROPRIEDADE: DESENVILVIDA EM SALA DE AULA
#UTILIZADA EM CONJUNTO COM AS CLASSES BOI E CRUD
#ATUALMENTE NÃO UTILIZADA
class Propriedade:
    def __init__(self, prop_id, proprietario, endereco, cnpj):
        self._id = prop_id
        self._proprietario = proprietario
        self._endereco = endereco
        self._cnpj = cnpj

    # Métodos Get
    def get_id(self):
        return self._id

    def get_proprietario(self):
        return self._proprietario

    def get_endereco(self):
        return self._endereco

    def get_cnpj(self):
        return self.cnpj

    # Métodos Set
    def set_id(self, novo_id):
        self._id = novo_id

    def set_proprietario(self, novo_proprietario):
        self._proprietario = novo_proprietario

    def set_endereco(self, novo_endereco):
        self._endereco = novo_endereco

    def set_cnpj(self, novo_cnpj):
        self._cnpj = novo_cnpj
