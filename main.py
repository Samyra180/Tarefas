import tkinter as tk
from tkinter import messagebox, font
import db  # Importa as funções do db.py
import sqlite3

frame_em_edicao = None

# Função para criar a janela de abertura
def janela_abertura():
    # Criar a janela de abertura
    splash = tk.Tk()
    splash.iconbitmap("imgs/list.ico")  # Define o ícone da janela
    splash.geometry("510x500")  # Tamanho da janela de abertura
    splash.title("Bem-vindo ao Organizador de Tarefas")

    # Definir cor de fundo suave
    splash.config(bg="#f0f0f0")  # Cor de fundo suave

    # Centralizar a janela de texto
    label = tk.Label(splash, text="Carregando...", font=("Arial", 24), bg="#f0f0f0", fg="#4CAF50")
    label.pack(expand=True)

    # Fechar a janela de abertura após 2 segundos e chamar a janela principal
    splash.after(2000, lambda: (splash.destroy(), janela_principal()))  # Fecha após 2 segundos e chama a janela principal

    splash.mainloop()



# Criar a janela principal
def janela_principal():
    janela = tk.Tk()
    janela.iconbitmap("imgs/list.ico")  # Define o ícone da janela
    janela.title("Organizador de tarefas")  # Define o título da janela
    janela.configure(bg="#F0F0F0")  # Cor de fundo da janela
    janela.geometry("510x500")  # Define o tamanho da janela
    janela.resizable(False, False)  # Bloqueia o redimensionamento da janela

    

    # Função para adicionar tarefa
    def adicionar_tarefa():
        global frame_em_edicao

        tarefa = entrada_tarefa.get().strip()
        if tarefa and tarefa != "Escreva sua tarefa aqui":
            if frame_em_edicao is not None:
                atualizar_tarefa(tarefa)
                frame_em_edicao = None
            else:
                db.adicionar_tarefa(tarefa)  # Salva a tarefa no banco de dados
                tarefa_id = db.obter_tarefas()[-1][0]  # Obtém o ID da última tarefa
                adicionar_item_tarefa((tarefa_id, tarefa))  # Adiciona a tarefa à lista na interface
                entrada_tarefa.delete(0, tk.END)
        else:
            messagebox.showwarning("Atenção", "Digite uma tarefa.")

    # Função para adicionar item da tarefa
    def adicionar_item_tarefa(tarefa):
        tarefa_id = tarefa[0]  # O ID da tarefa
        descricao_tarefa = tarefa[1]  # A descrição da tarefa

        frame_tarefa = tk.Frame(canvas_interior, bg="White", bd=1, relief=tk.SOLID)

        label_tarefa = tk.Label(frame_tarefa, text=descricao_tarefa, font=("Garamond", 16), bg="White", width=25, height=2, anchor="w")
        label_tarefa.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=5)

        # Botões de editar e deletar
        botao_editar = tk.Button(frame_tarefa, image=icon_editar, command=lambda f=frame_tarefa, l=label_tarefa, t_id=tarefa_id: preparar_edicao(f, l, t_id))
        botao_editar.pack(side=tk.RIGHT, padx=5)

        botao_deletar = tk.Button(frame_tarefa, image=icon_deletar, command=lambda f=frame_tarefa, tarefa_id=tarefa_id: deletar_tarefa(f, tarefa_id))
        botao_deletar.pack(side=tk.RIGHT, padx=5)

        frame_tarefa.pack(fill=tk.X, padx=5, pady=5)
        checkbutton = tk.Checkbutton(frame_tarefa, command=lambda label=label_tarefa: alterar_sublinhado(label))
        checkbutton.pack(side=tk.RIGHT, padx=5)

        canvas_interior.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    # Carregar tarefas do banco de dados ao iniciar
    def carregar_tarefas():
        tarefas = db.obter_tarefas()
        print(f"Tarefas carregadas: {tarefas}")  # Verifique as tarefas carregadas
        for tarefa in tarefas:
            adicionar_item_tarefa(tarefa)

    def preparar_edicao(frame_tarefa, label_tarefa, tarefa_id):
        global frame_em_edicao
        frame_em_edicao = frame_tarefa
        entrada_tarefa.delete(0, tk.END)
        entrada_tarefa.insert(0, label_tarefa.cget("text"))  # Carrega o texto da tarefa no campo de entrada

        # Armazena o ID da tarefa em edição
        global tarefa_em_edicao
        tarefa_em_edicao = tarefa_id

    def atualizar_tarefa(nova_tarefa):
        global frame_em_edicao, tarefa_em_edicao
        # Atualiza a tarefa no banco de dados
        db.atualizar_tarefa(tarefa_em_edicao, nova_tarefa)

        for widget in frame_em_edicao.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(text=nova_tarefa)  # Atualiza o texto da tarefa no label

    def alterar_sublinhado(label):
        fonte_atual = label.cget("font")
        if "overstrike" in fonte_atual:
            nova_fonte = fonte_atual.replace(" overstrike", "")
        else:
            nova_fonte = fonte_atual + " overstrike"
        label.config(font=nova_fonte)

    def deletar_tarefa(frame_tarefa, tarefa_id):
        # Deleta do banco de dados
        db.deletar_tarefa(tarefa_id)
        frame_tarefa.destroy()
        canvas_interior.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    # Conexão com o banco de dados
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()

    # Configuração da interface gráfica
    icon_editar = tk.PhotoImage(file="imgs/edit.png").subsample(15, 15)
    icon_deletar = tk.PhotoImage(file="imgs/delete.png").subsample(15, 15)

    # Título da aplicação
    fonte_cabecalho = font.Font(family="Garamond", size=24, weight="bold")
    rotulo_cabecalho = tk.Label(janela, text="Organizador de tarefas", font=fonte_cabecalho, bg="#F0F0F0", fg="#333333")
    rotulo_cabecalho.pack(pady=20)

    frame = tk.Frame(janela, bg="#F0F0F0")
    frame.pack(pady=10)

    entrada_tarefa = tk.Entry(frame, font=("Garamond", 14), relief=tk.FLAT, bg="white", fg="grey", width=30)
    entrada_tarefa.pack(side=tk.LEFT, padx=10)

    botao_adicionar = tk.Button(frame, command=adicionar_tarefa, text="Adicionar", bg="#4CAF50", fg="white", height=1, width=15, font=("Roboto", 11), relief=tk.FLAT)
    botao_adicionar.pack(side=tk.LEFT, padx=10)

    frame_lista_tarefas = tk.Frame(janela, bg="#F0F0F0")
    frame_lista_tarefas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    canvas = tk.Canvas(frame_lista_tarefas, bg="White")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame_lista_tarefas, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas_interior = tk.Frame(canvas, bg="White")
    canvas.create_window((0, 0), window=canvas_interior, anchor="nw")
    canvas_interior.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Inicializa o banco de dados e carrega as tarefas
    db.criar_tabela()
    carregar_tarefas()

    janela.mainloop()


# Chama a função para exibir a janela de abertura
janela_abertura()
