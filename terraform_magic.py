#!/usr/bin/env python3
import os
import sys
from pyfiglet import figlet_format
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint


text = "TerraMagic-cli"
cprint(figlet_format(text, font="big"), "magenta")

path = os.getcwd()
print(f'Voce está no diretório {path}')


def create_dir():
    while True:
        name_dir = str(input("Nome do projeto que deseja criar: "))
        if name_dir == '':
            continue
        else:
            try:
                os.mkdir(name_dir)
            except FileExistsError:
                print('Projeto já existe')
                continue
        print(f"{name_dir} criado com sucesso")
        response = str(input("Deseja criar outro ? S/N: "))
        if response == "S" or response == "s":
            create_dir()
        elif response == "N" or response == "n":
            os._exit
        else:
            print("Opção Inválida")
        return()


def create_files():
    print("-------------------------------------------")
    print("-- D = Directory -- F = file -- L = link --")
    print("-------------------------------------------")
    dir_list = os.listdir('.')
    for file in dir_list:
        if os.path.isfile(file):
            print('F-', file)
        elif os.path.isdir(file):
            print('D-', file)
        elif os.path.islink(file):
            print('L-', file)
        else:
            print('---', file)

    path = str(input("Escolha a pasta para criar os Terraform files: "))
    if path in dir_list:
        os.chdir(path)
        print(f"Existem {len(os.listdir('.'))} arquivos nesse diretório")
        file_list = [
            'provider.tf',
            'terraform.tfvars',
            'backend.tf',
            'vars.tf',
            '.gitignore',
            'ec2.tf',
            'output.tf'
            ]
        while True:
            default_files = str(input("Criar arquivos para AWS ? S(Sim) ou N(Sair): "))
            if default_files == "S" or default_files == "s":
                for filename in file_list:
                    all = open(filename, 'w+')
                    print(f'Os seguintes arquivos foram criados: {filename}')
                break
            elif default_files == "N" or default_files == "n":
                print("Você não criou o Terraform Files")
                break
            else:
                print("Opção Inválida")
    elif path not in dir_list:
        response = str(input("O Projeto não existe, deseja criar-lo S/N: "))
        if response == "S" or response == "s":
            create_dir()
            create_files()
        elif response == "N" or response == "n":
            print('Você optou por não continuar :( ')
        else:
            print('Você não informou uma opção válida')
    else:
        os._exit
    return()


try:
    create_dir()
    create_files()
except(KeyboardInterrupt):
    print(" Você pressionou Ctrl+C, até Logo!")
