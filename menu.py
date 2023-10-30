from classe_boi import Boi
from propriedade import Propriedade  # Importe a classe Propriedade
import connection as db

class Menu:
    def exibir_menu(self):
        print("\n----- MENU -----")
        print("1. Adicionar Boi")
        print("2. Listar Bois")
        print("3. Buscar Boi")
        print("4. Atualizar Boi")
        print("5. Remover Boi")
        print("6. Adicionar Propriedade")
        print("7. Listar Propriedades")
        print("8. Buscar Propriedade")
        print("9. Atualizar Propriedade")
        print("10. Remover Propriedade")
        print("0. Sair")

    def obter_input(self, mensagem):
        return input(mensagem)

    def executar(self):
        while True:
            self.exibir_menu()
            escolha = self.obter_input("Escolha uma opção: ")
    
            if escolha == "1":
                # Adicionar Boi
                peso = float(self.obter_input("Digite o Peso do Boi: "))
                idPropriedade = int(self.obter_input("Digite o ID da Propriedade: "))
                novo_boi = Boi(peso, idPropriedade)
                db.inserir_boi(novo_boi.get_peso(), novo_boi.get_idPropriedade())
    
            elif escolha == "2":
                # Listar Bois
                resultados = db.select_tabela(0)
                for linha in resultados:
                    novo_boi = Boi.construtor_alternativo(linha[0], linha[1], linha[2])
                    print(novo_boi.get_info())
    
            elif escolha == "3":
                # Buscar Boi
                num_busca = int(self.obter_input("Digite o Número do Boi a ser buscado: "))
                boi_encontrado = db.select_only(0, num_busca)
                novo_boi = Boi.construtor_alternativo(boi_encontrado[0], boi_encontrado[1], boi_encontrado[2])
                if boi_encontrado:
                    print("Boi encontrado:", novo_boi.get_info())
                else:
                    print("Boi não encontrado.")
    
            elif escolha == "4":
                # Atualizar Boi
                num_atualizar = int(self.obter_input("Digite o Número do Boi a ser atualizado: "))
                novo_peso = float(self.obter_input("Digite o novo Peso do Boi: "))
                db.update_tabela(0, num_atualizar, novo_peso, None)
    
            elif escolha == "5":
                # Remover Boi
                num_remover = int(self.obter_input("Digite o Número do Boi a ser removido: "))
                db.deletar_tabela(0, num_remover)
    
            elif escolha == "6":
                # Adicionar Propriedade
                nome = self.obter_input("Digite o Nome da Propriedade: ")
                endereco = self.obter_input("Digite o Endereço da Propriedade: ")
                cnpj = self.obter_input("Digite o CNPJ da Propriedade: ")
                nova_propriedade = Propriedade(nome, endereco, cnpj)  # Crie uma nova instância de Propriedade
                db.inserir_propriedade(nova_propriedade.get_nome(), nova_propriedade.get_endereco(), nova_propriedade.get_cnpj())
    
            elif escolha == "7":
                # Listar Propriedades
                resultados = db.select_tabela(1)
                for linha in resultados:
                    nova_propriedade = Propriedade.construtor_alternativo(linha[0], linha[1], linha[2], linha[3])
                    print(nova_propriedade.get_info())
    
            elif escolha == "8":
                # Buscar Propriedade
                id_busca = int(self.obter_input("Digite o ID da Propriedade a ser buscada: "))
                propriedade_encontrada = db.select_only(1, id_busca)
                if propriedade_encontrada:
                    nova_propriedade = Propriedade.construtor_alternativo(propriedade_encontrada[0], propriedade_encontrada[1], propriedade_encontrada[2], propriedade_encontrada[3])
                    print("Propriedade encontrada:", nova_propriedade.get_info())
                else:
                    print("Propriedade não encontrada.")
    
            elif escolha == "9":
                # Atualizar Propriedade
                id_atualizar = int(self.obter_input("Digite o ID da Propriedade a ser atualizada: "))
                novo_proprietario = self.obter_input("Digite o novo Nome da propriedade: ")
                db.update_tabela(1, id_atualizar, None, novo_proprietario)
    
            elif escolha == "10":
                # Remover Propriedade
                id_remover = int(self.obter_input("Digite o ID da Propriedade a ser removida: "))
                db.deletar_tabela(1, id_remover)
    
            elif escolha == "0":
                print("Saindo do programa. Até mais!")
                break
            
            else:
                print("Opção inválida. Tente novamente.")
    