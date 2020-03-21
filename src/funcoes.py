import os
import sys

class Cadastro():
    def cadastro_usuario(self=None):
        user = str(input("Digite o nome do usuário: \n"))
        password = str(input("Digite a a senha: \n"))
        confirmar_user = str(input("Deseja criar o usuário? \n"))

        try:
            if confirmar_user == 'sim' or confirmar_user == 's' or confirmar_user == 'SIM' or confirmar_user == 'Sim':
                os.system("net user" + " " + user + " " + password + " " + "/add")
                print(f"Usuário {user} criado com sucesso.")
            elif confirmar_user == 'nao' or confirmar_user == 'n' or confirmar_user == 'NAO' or confirmar_user == 'Nao':
                print("Cancelando operação. \n")
            else:
                print("Comando não reconhecido. \n")
        except:
            print("Operação não realizada, tente novamente. \n")

    def add_admin(self=None):
        user = str(input("Digite o nome do usuário: \n"))
        confirmar_user = str(input("Deseja adicionar o usuário ao grupo de Administradores? \n"))

        try:
            if confirmar_user == 'sim' or confirmar_user == 's' or confirmar_user == 'SIM' or confirmar_user == 'Sim':
                os.system("net localgroup Administradores" + " " + user + " " + "/add")
                print(f"Usuário {user} cadastrado como administrador com  sucesso. \n")
            elif confirmar_user == 'nao' or confirmar_user == 'n' or confirmar_user == 'NAO' or confirmar_user == 'Nao':
                print("Cancelando operação. \n")
            else:
                print("Comando não reconhecido! \n")
        except:
            print("Operação não realizada, tente novamente. \n")

class Listar():
    def listar_usuarios(self=None):
        operacao = str(input("Deseja listar os usuarios? \n"))
        if operacao == 'sim' or operacao == 's' or operacao == 'Sim' or operacao == 'S':
            os.system("net user")
        else:
            print("Comando não reconhecido! \n")
    
    def listar_admins(self=None):
        operacao = str(input("Deseja listar os Administradores? \n"))
        if operacao == 'sim' or operacao == 's' or operacao == 'Sim' or operacao == 'S':
            os.system("net localgroup Administradores")
        else:
            print("Comando não reconhecido. \n")
    
class Deletar():
    def deletar_user(self=None):
        user = str(input("Digite o nome do usuario que deseja deletar: \n"))
        operacao = str(input(f"Deseja deletar o usuario {user}? \n"))
        if operacao == 'sim' or operacao == 's' or operacao == 'Sim' or operacao == 'S':
            os.system(f"net user {user} /delete")
            print(f"Usuário {user} deletado com sucesso.")
        else:
            print("Comando não reconhecido. \n")

    def deletar_admin(self=None):
        user = str(input("Digite o nome do usuairo que deseja: \n"))
        operacao = str(input(f"Deseja remover {user} do grupo de Administradores? \n"))
        if operacao == 'sim' or operacao == 's' or operacao == 'Sim' or operacao == 'S':
            os.system(f"net localgroup Administradores {user} /delete")
        else:
            print("Comando não reconhecido. \n")

class Sair():
    def sair(self=None):
        print("Fim da execução... ")
        os.sys.exit()