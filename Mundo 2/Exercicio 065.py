# soma = 0
# contador = 0
# maior = 0
# menor = 0
# while True:
#     n = int(input('Entre com um número: '))
#     c = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
#     if c == 'N':
#         break
#     else:
#         print('Continuando...')
#     soma = soma + n
#     contador = contador + 1
#     if n == 1:
#         maior = n
#         menor = n
#     else:
#         if n > maior:
#             maior = n
#         if n < menor:
#             menor = n
# media = soma / contador
# print(f'A soma dos números é: {soma}')
# print(f'A média dos números é: {media:.2f} e foram digitados: {contador} números.')
# print(f'O maior número é: {maior} e o menor número é: {menor}')


# soma = 0
# cont = 0
# maior = 0
# menor = 0
# while True:
#     num = int(input(f'Entre com um número: '))
#     ent = str(input(f'Deseja continuar? [S / N]: ')).strip().upper()[0]
#     if ent == 'N':
#         break
#     else:
#         print(f'Continuando...')
#     soma = soma + num
#     cont = cont + 1
#     if num == 1:
#         maior = num
#         menor = num
#     else:
#         if num > maior:
#             maior = num
#         if num < menor:
#             menor = num
# media = soma / cont
# print(f'A soma dos números é: {soma}')
# print(f'A media dos números é: {media:.2f} Foram digitados: {cont} números.')
# print(f'O maior número foi {maior} e o menor números é {menor}')


# soma = 0
# cont = 0
# maior = None
# menor = None

# while True:
#     num = int(input(f'Entre com um número: '))
#     ent = str(input(f'Deseja continuar? [S / N]: ')).strip().upper()[0]
#     soma += num
#     cont += 1
    
#     if maior is None or num > maior:
#         maior = num
#     if menor is None or num < menor:
#         menor = num
    
#     if ent == 'N':
#         break
#     else:
#         print(f'Continuando...')

# media = soma / cont
# print(f'A soma dos números é: {soma}')
# print(f'A média dos números é: {media:.2f}. Foram digitados: {cont} números.')
# print(f'O maior número foi {maior} e o menor número é {menor}')


# soma = 0
# cont = 0
# maior = None
# menor = None

# while True:
#     num = int(input(f'Entre com o valor: '))
#     ent = str(input(f'Deseja continuar ? [S / N]: ')).upper().strip()[0]
   
#     if maior is None or num > maior:
#         maior = num
#     if menor is None or num < menor:
#         menor = num

#     if ent == 'N':
#             break
#     else:
#         print(f'Continuando...')
        
   

#     soma = soma + num
#     cont = cont + 1
#     media = soma / cont

#     print(f'A soma do valores é: {soma} e a quantidade de entradas foram {cont}.')
#     print(f'Media dos valore foi de {media}.')
#     print(f'Maior valor de entrada foi {maior} e o menor foi {menor}')




# soma = 0
# cont = 0
# maior = None
# menor = None

# while True:
#     num = int(input(f'Entre com um número: '))
#     ent = str(input(f'Deseja continuar? [S / N]: ')).strip().upper()[0]

#     soma = soma + num
#     cont = cont + 1
#     media = soma / cont
    
#     if maior is None or num > maior:
#         maior = num
#     if menor is None or num < menor:
#         menor = num
    
#     if ent == 'N':
#         break
#     else:
#         print(f'Continuando...')

# print(f'A soma dos números é: {soma}')
# print(f'A média dos números é: {media:.2f}. Foram digitados: {cont} números.')
# print(f'O maior número foi {maior} e o menor número é {menor}')


soma = 0
cont = 0
maior = None
menor = None

while True:
    numero = int(input(f'Entre com o valor: '))
    entrada = (input(f'Deseja continuar? [S / N]: ')).upper().strip()[0]

    soma = soma + numero
    cont = cont + 1
    media = soma / cont

    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero

    if entrada == 'N':
        break
    else:
        print(f'Continuando...')

print(f'A soma dos valores é: {soma} e a quantidade de entradas foram {cont}')
print(f'a media foi de {media:.1f}')
print(f'O maior valor foi {maior} e o menor {menor}')




