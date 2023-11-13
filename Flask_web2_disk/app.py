# 04/11/2023

from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

lista = []

@app.get("/")
def home():
    load_file()
    return render_template("base.html", lista_front=lista)


@app.post("/add")
def add():
    user = []    
    nome  = request.form.get("nome")
    fone  = request.form.get("fone")
    email = request.form.get("email")
    if nome != '' and fone != '' and email != '':        
        user.append(nome)
        user.append(fone)
        user.append(email)
        lista.append(user)        
        print(f'Add: {lista}')
        gravar_lista()              
    else:
        print('** Usuário não cadastrato, todos os dados devem ser fornecidos **')    
    return redirect(url_for("home"))


@app.post("/sort")
def sort():
    if lista != []:
        print(f'** Ordenando a lista **')
        lista.sort()
        gravar_lista()
    return redirect(url_for("home"))


@app.post("/reverse")
def reverse():
    if lista != []:
        print(f'** Invertendo a lista **')
        lista.reverse()
        gravar_lista()
    return redirect(url_for("home"))


@app.post("/clear")
def clear():
    global lista
    if lista != []:       
        lista = []
        gravar_lista()
    return redirect(url_for("home"))


# @app.get("/update/<lista_nome>")
# def update(lista_nome):    
    # return redirect(url_for("home"))


@app.get("/delete/<lista_nome>")
def delete(lista_nome):
    nome = lista_nome
    for i in range(len(lista)):
        if nome in lista[i]:            
            del lista[i]
            break
    gravar_lista()
    return redirect(url_for("home"))


def gravar_lista():
    ref = 0
    try:        
        file_txt = open('agenda.txt', 'w', encoding='UTF-8')
        file_csv = open('agenda.csv', 'w')
        for itens in lista:
            for item in itens:               
                file_txt.write(f'{item};')
                file_csv.write(f'{item};')                       
            file_txt.write(f'\n')
            file_csv.write(f'\n')           

        file_txt.close()
        file_csv.close()
        print('** Arquivo gravado com sucesso **')        
    except:
        print('** Erro ao gravar arquivo **')


def load_file():
    arquivo = 'agenda.csv'
    if os.path.exists(arquivo):
        global lista
        lis = []    
        try:        
            with open('agenda.csv', 'r', encoding='UTF-8') as file:
                lis = [item.split(';') for item in file.readlines()]
                print(f'lis: {lis}')
                
                for item in lis:
                    for j in range(len(item)):
                        if item[j] == '\n':
                            item.pop()

                for i in range(len(lis)):
                    for j in range(len(lis[i])):
                        lis[i][j] = lis[i][j].replace('\n','')

                lista = lis.copy()
            file.close()        
            print(f'lista: {lista}')           
            print('** Arquivo carregado com sucesso **')            
        except:
            print('** Erro ao carregar arquivo **')
    else:
        print('** Não existe o arquivo "agenda.csv" **')

        

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)