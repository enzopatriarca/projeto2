
while True:
    numero1 = input('Digite um numero: ')
    numero2 = input('Digite outro numero: ')
    operador = input('Digite um operador (+-*/)')
    numeros_validos = None
    try:
        num_1 = float(numero1)
        num_2 = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None
        # print(error)
    
    if numeros_validos == None:
        print('Um dos numeros nao é valido')
        continue

   
    operadores_per = '+-*/'

    if operador not in operadores_per:
        print('Operador invalido')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    resultado = 0

    if operador == '+':
        resultado = num_1 + num_2
    elif operador == '-':
        resultado = num_1 - num_2
    elif operador == '*':
        resultado = num_1 * num_2
    elif operador == '/':
        resultado = num_1 / num_2
    
    print('Resultado da operacao: ', resultado)

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair == True:
        break
    print(sair) 