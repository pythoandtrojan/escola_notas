import os 

def clear():
    os.system('clear')

def cadastro():
    while True:
        try:
            print("1. entrar")
            print("2. admin")
            print("3. sair")
            escolha = int(iput("escolha: "))
            if escolha == 1:
                
