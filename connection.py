#O ALGORITMO ABAIXO FAZ UMA CONEXÃO COM O BANCO DE DADOS MYSQL
#CRIADO EXTERNAMENTE À SALA DE AULA
#UTILIZADO
#POSSUI MÉTODOS GENÉRICOS QUE PODEM SER UTILIZDOS TANTO PARA
#TRABALHAR COM A TABELA BOI, QUANTO COM A TABELA PROPRIEDADE
#SALVO O MÉTODO DE INSERT QUE UTILIZAM DIFERENTES QUANTIDADES DE PARÂMETROS
#CRUD GENÉRICO BÁSICO

import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='coloque sua senha aqui',
        database='fazenda'
    )
    return conexao

def inserir_propriedade(nome, cnpj, endereco):
    conexao = conectar()
    cursor = conexao.cursor()
    inserir = "INSERT INTO propriedade (nome, cnpj, endereco) VALUES (%s, %s, %s)"
    dados = (nome, cnpj, endereco)
    cursor.execute(inserir, dados)
    conexao.commit()
    cursor.close()
    conexao.close()

def inserir_boi(peso, idPropriedade):
    conexao = conectar()
    cursor = conexao.cursor()
    inserir = "INSERT INTO bois (peso, idPropriedade) VALUES (%s, %s)"
    dados = (peso, idPropriedade)
    cursor.execute(inserir, dados)
    conexao.commit()
    cursor.close()
    conexao.close()

def select_tabela(numero):
    conexao = conectar()
    cursor = conexao.cursor()
    
    if numero == 0:
        cursor.execute("SELECT * FROM bois")
        resultados = cursor.fetchall()
        print("\nTabela Bois:")
        for linha in resultados:
            print(linha)
    elif numero == 1:
        cursor.execute("SELECT * FROM propriedade")
        resultados = cursor.fetchall()
        print("\nTabela Propriedade:")
        for linha in resultados:
            print(linha)

    cursor.close()
    conexao.close()

def select_only(numero, id):
    conexao = conectar()
    cursor = conexao.cursor()
    
    if numero == 0:
        cursor.execute(f"SELECT * FROM bois where id= {id}")
        resultados = cursor.fetchall()
        for linha in resultados:
            return linha
    elif numero == 1:
        cursor.execute(f"SELECT * FROM propriedade where id= {id} ")
        resultados = cursor.fetchall()
        for linha in resultados:
            return linha
    cursor.close()
    conexao.close()


def update_tabela(numero, id, novo_peso, novo_nome):
    conexao = conectar()
    cursor = conexao.cursor()
    
    if numero == 0:
        atualizar = "UPDATE bois SET peso = %s WHERE id = %s"
        dados = (novo_peso, id)
    elif numero == 1:
        atualizar = "UPDATE propriedade SET nome = %s WHERE id = %s"
        dados = (novo_nome, id)
    
    cursor.execute(atualizar, dados)
    conexao.commit()
    cursor.close()
    conexao.close()

def deletar_tabela(numero, id):
    conexao = conectar()
    cursor = conexao.cursor()
    
    if numero == 0:
        deletar = "DELETE FROM bois WHERE id = %s"
    elif numero == 1:
        deletar = "DELETE FROM propriedade WHERE id = %s"
    
    cursor.execute(deletar, (id,))
    conexao.commit()
    cursor.close()
    conexao.close()
