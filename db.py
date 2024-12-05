import sqlite3
from datetime import datetime

# Função para conectar ao banco de dados
def conectar():
    return sqlite3.connect("tarefas.db")

# Função para criar a tabela de tarefas se ela não existir
def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tarefas (id INTEGER PRIMARY KEY AUTOINCREMENT,descricao TEXT NOT NULL)")
    conexao.commit()
    conexao.close()

# Função para adicionar uma tarefa
def adicionar_tarefa(descricao):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO tarefas (descricao) VALUES (?)", (descricao,))
    conexao.commit()
    print(f"Tarefa adicionada: {descricao}") 
    conexao.close()


# Função para pegar todas as tarefas
def obter_tarefas():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conexao.close()

    for tarefa in tarefas:
        print(f"Tarefa ID: {tarefa[0]}, Descrição: {tarefa[1]}")  # Verifique a descrição
    return tarefas


# Função para deletar uma tarefa
def deletar_tarefa(id_tarefa):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id=?", (id_tarefa,))
    conexao.commit()
    conexao.close()


# Função para atualizar uma tarefa
def atualizar_tarefa(id_tarefa, nova_descricao):
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()
    cursor.execute("UPDATE tarefas SET descricao = ? WHERE id = ?", (nova_descricao, id_tarefa))
    conexao.commit()
    conexao.close()




