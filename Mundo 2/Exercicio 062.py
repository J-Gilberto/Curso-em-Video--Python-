# n1 = int(input(f'Entre com o termo: '))
# n2 = int(input(f'Entre com a razão: '))

# termo = n1
# contador = 1
# total = 0
# mais = 10

# while mais != 0:
#     total = total + mais
    
#     while contador <= total:
#         print(f'{termo} - ', end='')
#         termo = termo + n2
#         contador = contador + 1
#     print(f'Pausa!')
#     mais = int(input(f'Entre com a quantidade dos novos termos: '))
# print(f'Total de termos foi: {total}')
# print(f'Fim do programa !')



# n1 = int(input(f'Entre com o termo: '))
# n2 = int(input(f'Entre com a razão: '))
# print(f'~~~~'*10)

# termo = n1
# contador = 1
# total = 0
# mais = 10

# while mais != 0:
#     total = total + mais
    
#     while contador <= total:
#         print(f'{termo} - ', end='')
#         termo = termo + n2
#         contador = contador + 1
#     print('Pausa')
#     print(f'~~~~'*10)
#     mais = int(input(f'Entre com novos termos: '))
# print(f'Total de termos foi de {total}')
# print(f'Fim do programa!')

n1 = int(input(f'Entre com o termo: '))
n2 = int(input(f'Entre com a razão: '))

termo = n1
contador = 1
total = 0
mais = 10

while mais != 0:
    
    total = total + mais
    
    while contador <= total:
        print(f'{termo} - ', end='')
        termo = termo + n2
        contador = contador + 1
    print(f'Pausa')
    mais = int(input(f'Entre com os novos termos: '))
print(f'O total de termos foi: {total}')
print(f'Fim do programa !')