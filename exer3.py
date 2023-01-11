"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_str = input(
    'Digite um numero inteiro:\n'
)

try:
    numero = int(numero_str)
    if numero % 2 == 0:
        print ('É um numero par')
    else:
        print('É um numero impar')
    # print('FLOAT:', numero_float)
    # print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input('Digite um horario\n')

try:
    horario_int= int(horario)
    if horario_int >= 0 and horario_int <= 11:
        print('Bom dia')
    elif horario_int >= 12 and horario_int <= 17:
        print('Boa tarde')
    elif horario_int >= 18 and horario_int <= 23:
        print('Boa noite')
    else:
        print('Horario digitado nao existe')
except:
    print('Isso não é um número inteiro!')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

Nome = input('Digite seu nome\n')
tam = len(Nome)

if tam <= 4:
    print("seu nome e curto")
elif tam == 5 or tam == 6:
    print('seu nome é normal')
elif tam > 6:
    print('seu nome e longo')
