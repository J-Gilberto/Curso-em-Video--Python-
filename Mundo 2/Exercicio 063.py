#Exercício Python 63: Escreva um programa que leia um número N inteiro 
# qualquer e mostre na tela os N primeiros elementos de uma Sequência 
# de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

# n = int(input(f'Entre com a quantidade de termos: '))
 
# t1 = 0
# t2 = 1
# cont = 3
# print(f'{t1} - {t2}', end='')

# while cont <= n:
#     t3 = t1 + t2
#     print(f' - {t3}', end='')
#     t1 = t2
#     t2 = t3
#     cont = cont + 1
# print(f' - Fim')


# m = int(input(f'Entre comma quantidade de termos: '))

# t1 = 0
# t2 = 1
# cont = 3

# print(f'{t1} - {t2}', end='')

# while cont <= m:
#     t3 = t1 + t2
#     print(f' - {t3}', end='')
#     t1 = t2
#     t2 = t3
#     cont = cont + 1
# print(f' - Fim')
    
    
k = int(input(f'Entre com a quantidade de termos: '))

t1 = 0
t2 = 1
cont = 3
print(f'{t1} - {t2}', end='')
while cont <= k:
    t3 = t1 + t2
    print(f' - {t3}', end='')
    cont = cont + 1
    t1 = t2
    t2 = t3
print(f' - Fim')
    
    
