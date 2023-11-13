# Agenda gravando e lendo arquivo CSV
# Finalizado 01/nov/2023

from click import clear
from os import system
import sys

dic = {}

def menu():
    try:
        while True:
            system('clear')
            print('\n** Agenda **\n')
            print('1. Cadastrar usuário')
            print('2. Mostrar dados de um usuário')
            print('3. Listar todos nomes cadastrados')
            print('4. Remover usuário')
            print('5. Limpar toda agenda')
            print('6. Ler arquivo')
            print('7. Sair')
            op = int(input('\nOpção: '))
            return op 
    except:
        pass   
        

def cadastrar_usuario():
    system('clear')
    print('\n** Cadastrar usuário **')
    nome = input("\nNome: ")
    fone = input("Telefone: ")
    email = input('E-mail: ')
    if nome != '' and fone != '' and email != '':
        dic[nome] = {'fone': fone, 'email':email}
        print('\n** Usuário cadastrato com sucesso! **')
        gravar_agenda()
        input('\nPressione Enter para continuar.')
    else:
        print('\n** Usuário não cadastrato, todos os dados devem ser fornecidos **')        
        input('\nPressione Enter para continuar.')


def buscar_usuario():
    ref = listar_todos_usuarios(True)
    if ref:
        user = input('\nQual usuário deseja listar dados? ')
        if user in dic.keys():
            print(f"\nFone  : {dic[user]['fone']}")
            print(f"E-mail: {dic[user]['email']}")
            input('\nPressione Enter para continuar.')
        elif user.isdigit():
            index = int(user)            
            if index > 0 and index < len(dic)+1:
                for num, nome in enumerate(dic.keys()):
                    if num+1 == index:
                        print(f"\nNome  : {nome}")
                        print(f"Fone  : {dic[nome]['fone']}")
                        print(f"E-mail: {dic[nome]['email']}")
            input('\nPressione Enter para continuar.')
        else:
            print('\nUsuário não cadastrado')
            input('\nPressione Enter para continuar.')


def listar_todos_usuarios(ref=False):
    clear()
    if dic == {}:
        print('\n** Nao há usuário cadastrado! **')
        input('\nPressione Enter para continuar.')
        return False
    else:
        print()
        for number, user in enumerate(dic.keys()):
            print(f'{number+1}. {user}')
        if ref:
            return True
        input('\nPressione Enter para continuar.')


def remover_usuario():
    ref = listar_todos_usuarios(True)
    try:
        if ref:
            user = input('\nQual usuário deseja remover? ')        
            if user in dic.keys():
                op = input(f'\nUsuário "{user}" será removido. Continuar? [N/s]: ')
                if op == 's':
                    del dic[user]
                gravar_agenda()        
            elif user.isdigit():
                index = int(user)            
                if index > 0 and index < len(dic)+1:                    
                    for num, nome in enumerate(dic.keys()):
                        if num+1 == index:
                            op = input(f'\nUsuário "{user}. {nome}" será removido. Continuar? [N/s]: ')
                            if op == 's':
                                del dic[nome]
                                gravar_agenda()
                            break                                
            else:
                print('\nUsuário não cadastrado')
                input('\nPressione Enter para continuar.')
    except:
        pass
    

def limpar_agenda():
    global dic
    ref = listar_todos_usuarios(True)
    if ref:
        op = input('\nToda a agenda será apagada. Continuar? [N/s] ')
        if op == 's':
            dic = {}
            gravar_agenda()
            print('\n** Todos registros foram apagados **')
            input('\nPressione Enter para continuar.')
            

def gravar_agenda():
    try:        
        file = open('grava-agenda.csv', 'w')
        for nome in dic.keys():
            file.write(f"{nome};")
            file.write(f"{dic[nome]['fone']};")
            file.write(f"{dic[nome]['email']}\n")
        file.close()        
    except:
        print('\n** Erro ao gravar arquivo **')        
        print('\n** Arquivo não pode estar aberto **')        


def ler_agenda(ref=False):
    try:       
        with open('grava-agenda.csv', 'r') as file:
            lista = [item for item in file.readlines()]
        file.close()
        for i in range(len(lista)):
            lista[i] = lista[i].replace('\n', '')
            nome  = lista[i].split(';')[0]
            fone  = lista[i].split(';')[1]
            email = lista[i].split(';')[2]
            dic[nome] = {'fone': fone, 'email':email}
        if ref:
            clear()
            print('\n** Agenda atualizada **')
            input('\nPressione Enter para continuar.')
    except:
        if ref:
            clear()
            print('\n** Não há agenda gravada **')
            input('\nPressione Enter para continuar.')
        else:
            pass


def sair():
    gravar_agenda()
    print()
    sys.exit()


#********************************************************************


if __name__ == '__main__':
    try:
        ler_agenda()
        while True:
            clear()
            op = menu()    
            match op:
                case 1:
                    cadastrar_usuario()
                case 2:
                    buscar_usuario()
                case 3:
                    listar_todos_usuarios()
                case 4:
                    remover_usuario()
                case 5:
                    limpar_agenda()
                case 6:
                    ler_agenda(True)
                case 7:
                    sair()
                case _:
                   pass
    # Excessão gerada pelo sys.exit() [SystemExit]
    except SystemExit:
        sys.exit()           
