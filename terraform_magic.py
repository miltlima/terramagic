# Name : Project Make dir Terraform
# Author Milton Lima
# Release: beta
# Version: 0.0.1

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
        name_dir = str(input("Informe o nome do projeto que deseja criar: "))
        if name_dir == '':
            continue
        else:
            try:
                os.mkdir(name_dir)
            except FileExistsError:
                print('A pasta do projeto já existe')
                continue
        print(f"Pasta do projeto criada com sucesso {name_dir}")
        response = str(input("Deseja criar outro ? S/N ou qualquer tecla para sair: "))
        if response == "S" or response == "s":
            create_dir()
        elif response == "N" or response == "n":
            os._exit
        else:
            print("Opção Inválida")
        return()


def create_files():
    dir_list = os.listdir('.')
    for file in dir_list:
        print(file)
    path = str(input("Informe qual Projeto você deseja criar esses arquivos: "))
    if path in dir_list:
        os.chdir(path)
        print(f"Arquivos atuais do direrório {os.listdir('.')}")
        terraform_files = ['provider.tf', 'terraform.tfvars', 'backend.tf', 'vars.tf', '.gitignore', 'ec2.tf', 'output.tf']
        default_files = str(input("Deseja criar os arquivos default Terraform para AWS ? "))
        if default_files == "S" or default_files == 's':
            for filename in terraform_files:
                all = open(filename, 'w+')
                print(f'Os seguintes arquivos foram criados: {filename}')
        else:
            print("Opção Invalida")
    elif path not in dir_list:
        response = str(input("O Projeto não existe, deseja criar-lo S/N: "))
        if response == "S" or response == "s":
            create_dir()
        elif response == "N" or response == "n":
            print('Você optou por não continuar :( ')
        else:
            print('Você não informou uma opção valida')
    else:
        os._exit
    return()


create_dir()
create_files()
