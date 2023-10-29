#ESQUEMA INTERAÇÃO COM O USUÁRIO VIA TERMINAL
#EXECUTA OS MÉTODOS BÁSICOS CRIADOS NO ARQUIVO CONNECTION
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
                peso = int(self.obter_input("Digite o PESO do Boi: "))
                id = float(self.obter_input("Digite o ID DA PROPRIEDADE do Boi: "))
                db.inserir_boi(peso, id)

            elif escolha == "2":
                db.select_tabela(0)

            elif escolha == "3":
                num_busca = int(self.obter_input("Digite o Número do Boi a ser buscado: "))
                boi_encontrado = db.select_only(0, num_busca)
                if boi_encontrado:
                    print("Boi encontrado:", boi_encontrado)
                else:
                    print("Boi não encontrado.")

            elif escolha == "4":
                num_atualizar = int(self.obter_input("Digite o Número do Boi a ser atualizado: "))
                novo_peso = float(self.obter_input("Digite o novo Peso do Boi: "))
                db.update_tabela(0, num_atualizar, novo_peso, None)

            elif escolha == "5":
                num_remover = int(self.obter_input("Digite o Número do Boi a ser removido: "))
                db.deletar_tabela(0, num_remover)

            elif escolha == "6":
                nome = self.obter_input("Digite o Nome da Propriedade: ")
                endereco = self.obter_input("Digite o Endereço da Propriedade: ")
                cnpj = self.obter_input("Digite o CNPJ da Propriedade: ")
                db.inserir_propriedade(nome, cnpj, endereco)

            elif escolha == "7":
                db.select_tabela(1)

            elif escolha == "8":
                id_busca = int(self.obter_input("Digite o ID da Propriedade a ser buscada: "))
                propriedade_encontrada = db.select_only(1)
                if propriedade_encontrada:
                    print("Propriedade encontrada:", propriedade_encontrada)
                else:
                    print("Propriedade não encontrada.")

            elif escolha == "9":
                id_atualizar = int(self.obter_input("Digite o ID da Propriedade a ser atualizada: "))
                novo_proprietario = self.obter_input("Digite o novo Nome da propriedade: ")
                db.update_tabela(1, id_atualizar, None, novo_proprietario)

            elif escolha == "10":
                id_remover = int(self.obter_input("Digite o ID da Propriedade a ser removida: "))
                db.deletar_tabela(1, id_remover)

            elif escolha == "0":
                print("Saindo do programa. Até mais!")
                break

            else:
                print("Opção inválida. Tente novamente.")
