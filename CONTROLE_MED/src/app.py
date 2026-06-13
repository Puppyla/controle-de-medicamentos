import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Carrega as variáveis do arquivo .env
load_dotenv()

# Pega a URL e a Chave de forma segura
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

# Cria a conexão oficial com o banco do grupo
supabase: Client = create_client(url, key)

medicamentos = []

def adicionar():
    nome = input("Nome do remédio: ")
    horario = input("Horário: ")

    if nome == "" or horario == "":
        print("Erro: dados vazios")
    else:
        medicamentos.append([nome, horario])
        print("Adicionado!")

def listar():
    if len(medicamentos) == 0:
        print("Nenhum medicamento")
    else:
        for i in range(len(medicamentos)):
            print(i, "-", medicamentos[i][0], "às", medicamentos[i][1])

def remover():
    i = int(input("Índice: "))
    if i < 0 or i >= len(medicamentos):
        print("Erro: índice inválido")
    else:
        medicamentos.pop(i)
        print("Removido!")
def editar():
    i = int(input("Índice: "))

    if i < 0 or i >= len(medicamentos):
        print("Erro: índice inválido")
    else:
        nome = input("Novo nome do remédio: ")
        horario = input("Novo horário: ")

        if nome == "" or horario == "":
            print("Erro: dados vazios")
        else:
            medicamentos[i] = [nome, horario]
            print("Medicamento atualizado!")

def menu():
    while True:
        print("\n1 - Adicionar")
        print("2 - Listar")
        print("3 - Remover")
        print("4 - Editar")
        print("5 - Sair")

        op = input("Escolha: ")

        if op == "1":
            adicionar()

        elif op == "2":
            listar()

        elif op == "3":
            remover()

        elif op == "4":
            editar()

        elif op == "5":
            break

        else:
            print("Opção inválida")

menu()
