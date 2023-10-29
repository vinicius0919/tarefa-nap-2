#CLASSE CRUD UTILIZADA PARA ADICIONAR OS OBJETOS DETRO DE UM ARRAY
#DESENVOLVIDO EM SALA DE AULA
#DADO QUE ESTÃOS ENDO ARMAZENADOS EM UM BANCO DE DADOS, NÃO ESTÁ MAIS SENDO UTILIZADA
class CRUD:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        if self.buscar_item('id', item.get_id()):
            print(f"Já existe um item com o ID {item.get_id()}. Não é possível adicionar.")
        else:
            self.itens.append(item)
            print(f"{item} adicionado com sucesso!")

    def listar_itens(self):
        print("\n-----_---LISTA DE ITENS-------------")
        for item in self.itens:
            print(item.__dict__)

    def buscar_item(self, chave, valor):
        for item in self.itens:
            if getattr(item, chave) == valor:
                return item
        return None

    def atualizar_item(self, chave_busca, valor_busca, chave_atualizar, novo_valor):
        item_encontrado = self.buscar_item(chave_busca, valor_busca)
        if item_encontrado:
            setattr(item_encontrado, chave_atualizar, novo_valor)
            print(f"{item_encontrado} atualizado com sucesso!")
        else:
            print("Item não encontrado.")

    def remover_item(self, chave, valor):
        item_encontrado = self.buscar_item(chave, valor)
        if item_encontrado:
            self.itens.remove(item_encontrado)
            print(f"{item_encontrado} removido com sucesso!")
        else:
            print("Item não encontrado.")
