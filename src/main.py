import os
import sys
from funcoes import Cadastro, Deletar, Listar, Sair

while True:

    print("Bem vindo ao User Manager version 0.1 beta! \n")
    print("Dev by Black Hound. \n")

    menu = print("Menu: \n 1- Criar usuário.\n 2- Adicionar Administrador. \n 3- Listar usuários.\n 4- Listar Administradores. \n 5- Deletar usuários.\n 6- Sair.\n")

    operacao = str(input("O que deseja fazer? \n"))

    if operacao == '1':
        Cadastro.cadastro_usuario()

    if operacao == '2':
        Cadastro.add_admin()

    if operacao == '3':
        Listar.listar_usuarios()
    
    if operacao == '4':
        Listar.listar_admins()

    if operacao == '5':
        menu_deletar = print("Deseja: \n 1- Deletar um usuário.\n 2- Remover um usuário do grupo Administradores.\n 3- Sair.\n")
        op = str(input("O que deseja fazer? \n"))
        if op == '1':
            Deletar.deletar_user()
        elif op == '2':
            Deletar.deletar_admin()
        elif op == '3':
            Sair.sair()

    if operacao == '6':
        Sair.sair()
    





