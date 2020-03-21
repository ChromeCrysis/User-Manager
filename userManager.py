import os
import sys

print("Bem vindo ao User Manager version 0.1 beta!")
print("Desenvolvido por Black Hound.")

menu = print("Menu: \n 1- Criar usuário.\n 2- Listar usuários.\n 3- Deletar usuários.\n 4- Sair.\n")

operacao = str(input("O que deseja fazer? \n"))

if operacao == '1':
    user = str(input("Digite o nome de usuário: \n"))
    password = str(input("Digite a senha do usuário: \n"))
    confirmar_user = str(input("Deseja criar o usuário? \n"))
    try:
        if confirmar_user == 's' or confirmar_user == 'S' or confirmar_user == 'sim' or confirmar_user == 'SIM':
            os.system("net user" + " " + user + " " + password + " " + "/add")
            print(f"Usuário {user} cadastrado com sucesso!")
            confirmar_admin = str(input(f"Deseja tornar o usuário{user} administrador? \n"))
            if confirmar_admin == 's' or confirmar_admin == 'S' or confirmar_admin == 'sim' or confirmar_admin == 'SIM':
                os.system("net localgroup Administradores" + " " + user + " " + "/add")
                print(f"Usuário {user} cadastrado com sucesso como Administrador!")
            else:
                print("Não foi possível tornar Administador, por favor tente novamente!")
    except:
        print("Erro, não foi possível cadastrar o usuário. Tente novamente!")

if operacao == '2':
    print("Listar Usuários padrão ou Administradores? \n")
    op = str(input("Digite usuarios para listar Usuarios e administradores para listar Adminitradores \n"))
    if op == 'usuarios':
        try:
            confirmar_listar = str(input("Deseja listar os usuários? \n"))
            if confirmar_listar == 's' or confirmar_listar == 'S':
                os.system("net user")
        except:
            print("Não foi possível concluir, por favor tente novamente!")

    elif op == 'administradores':
        try:
            confirmar_listar = str(input("Deseja listar os Administradores? \n"))
            if confirmar_listar == 's' or confirmar_listar == 'S':
                os.system("net localgroup Administradores")
        except:
            print("Não foi possível concluir, por favor tente novamente!")
if operacao == '3':
    menu_deletar = print("Deseja: \n 1- Deletar um usuário.\n 2- Remover um usuário do grupo Administradores.\n 3- Sair.\n")
    op = str(input("O que deseja fazer? \n"))
    if op == '1':
        try:
            user_delete = str(input("Digite o nome do usuário que você deseja apagar: \n"))
            os.system(f"net user {user_delete} /delete")
            print(f"Usuário {user_delete} excluído com sucesso.")
        except:
            print("Não foi possível completar a exclusão, tente novamente.")
    if op =='2':
        try:
            adm_delete = str(input("Digite o nome do usuário que você deseja remover do grupo Administradores: \n"))
            os.system(f"net localgroup Administradores {adm_delete} /delete")
            print(f"Administrador {adm_delete} removido do grupo com sucesso.")
        except:
            print("Não foi possível completar a remoção, por favor tente novamente.")
    if op == '3':
        print("Encerrando o sistema.")
        os.sys.exit()

if operacao == '4':
    print("Encerrando o sistema.")
    os.sys.exit()
    





