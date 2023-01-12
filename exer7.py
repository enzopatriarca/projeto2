"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra = 'Eu te amo linda'
palavra_l = palavra.lower()
tentativas = ''
palavra_tentativa=''
count = 0
indice = range(0,len(palavra_l),1)

acertou = True
print(f'Adivinhe a palavra ou frase, ela contem {len(palavra)} caracteres\n')

while acertou:
    letra = input('Digite uma letra: ')
    print(letra)
    tam = len(letra)
    if tam > 1:
        print('Digite somente uma letra')
        continue
    if letra in palavra_l:
        if letra in tentativas:
            print('Voce ja tentou essa letra')
        else:
            if len(palavra_tentativa) == 0:
                for i in indice:
                    if letra == palavra_l[i]:
                        # print(i)
                        palavra_tentativa += palavra_l[i]
                        # print(palavra_tentativa)
                    else:
                        palavra_tentativa += '*'
            else:
                aux = ''
                for i in indice:
                    if letra == palavra_l[i]:
                        aux += palavra_l[i]
                    else:
                        aux += palavra_tentativa[i]
                palavra_tentativa = aux      
            tentativas +=letra
            count +=1;
            print(palavra_tentativa)
            if '*' not in palavra_tentativa:
                
                print('VOCE ACERTOU A PALAVRA!!')
                print(f'A frase era: {palavra} voce acertou com {count} tentativas')
                break
    else:
        count +=1;
        print(palavra_tentativa)
    
    
    # print(palavra)