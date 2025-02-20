soma = 0
contador = 0
maior = 0
menor = 0
while True:
    n = int(input('Entre com um número: '))
    c = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if c == 'N':
        break
    else:
        print('Continuando...')
    soma = soma + n
    contador = contador + 1
    if n == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / contador
print(f'A soma dos números é: {soma}')
print(f'A média dos números é: {media:.2f} e foram digitados: {contador} números.')
print(f'O maior número é: {maior} e o menor número é: {menor}')

