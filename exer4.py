
nome = 'Enzo Patriarca'
tam = len(nome)
nova_str = ''
i = 0
while i <= tam-1:
    nova_str += '*' + nome[i] 
    i = i+1

nova_str += '*'
print(nova_str)