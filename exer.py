primeiro_valor = input('Digite um 1 valor\n')
segundo_valor = input('Digite um 2 valor\n')

valor_1 = int(primeiro_valor)
valor_2 = int(segundo_valor)

if valor_1 >= valor_2:
    print(f'O valor 1 = "{valor_1}" é maior ou igual que o valor 2 = {valor_2}')
else:
    print(f'O valor 2 = "{valor_2}" é maior que o valor 1 = {valor_1}')