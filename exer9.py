"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

cpf = '74682489070'
nove_dig = cpf[:9]

lista = []
i=10
j=0
contador = 0
mult = 0
numeros = range(10, 1, -1)
for dig in nove_dig:
    dig_int=(int(dig))
    lista.append(dig_int)

while i !=1:
   for num in lista:
    # print(num,i)
    mult = i*num
    contador += mult
    i-=1
    
contador = contador *10
contador = contador%11
resultado = contador if contador <= 9 else 0

dez_dig = nove_dig + str(resultado)
segundo_resultado = 0
contador_regresivo = 11;
for digi in dez_dig:
    segundo_resultado += int(digi) * contador_regresivo
    contador_regresivo -=1

segundo_resultado = (segundo_resultado*10)%11
resultado_2 = 0 if segundo_resultado > 9 else segundo_resultado

novo_cpf = f'{nove_dig}{resultado}{resultado_2}'
if cpf == novo_cpf:
    print('CPF valido')
else:
    print('CPF invalido')



"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""
# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)