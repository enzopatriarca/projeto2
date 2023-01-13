"""
faça uma lista de compras com listas
i usuario dever ter a possibilidade de inserir, apagar e listar 
os valores da sua lista
Nao permita que o programa quebre com erros de indices inexistentes
 
"""
import os

Lista = []


while True:
    print('Selecione uma opçao: ')
    op = input('[i]nserir [a]pagar [l]istar ou [s]air: ')

    if(len(op) > 1):
        print('Selecione uma opçao valida')
        continue
    if op == 'i':
        os.system('cls') or None
        valor = input('Digite um item: ') 
        Lista.append(valor)
        os.system('cls') or None
        print('Valor adicionado com sucesso!')
        continue
    elif op == 'a':
        indice = input('Digite o indece a ser apagado: ')
        try:
            indice_int = int(indice)
            if (len(Lista) == 0):
                os.system('cls') or None
                print('A lista esta vazia nao ha nada para deletar.')
                continue
            Lista.pop(indice_int)
            os.system('cls') or None
            print('Item deletado com sucesso!')
        except ValueError:
            os.system('cls') or None
            print('Indice invalido, digite um numero inteiro!')
        except IndexError:
            print('Indice inserido nao existe')
        except Exception:
            print('Erro desconhecido')

    elif op == 'l':
        if len(Lista) >= 1:
            os.system('cls') or None
            print('Os itens na lista sao:')
            for indice, item in enumerate(Lista):
                print(indice, item)
                continue
        else: 
            os.system('cls') or None
            print('A lista esta vazia!')
            continue
    elif op == 's':
        break        

