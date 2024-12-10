from time import sleep

soma = 0
print('Programa de calcular numeros Pares !')
for numero in range(0, 6):
    num = int(input('Entre com numeros inteiros: '))
    print('=-='*10)
    if num % 2 == 0:
        soma = soma + num
sleep(2)
print(soma)


s = 0
for c in range (0, 6):
    name = int(input('Entre com numeros inteiros: '))
    if name % 2 == 0:
         s += name
print(s)
        
so = 0
for cont in range(0,6):
    ent = int(input('Entre com valores: '))
    if ent % 2 == 0:
        so = so + ent
print('Total de numeros inteiros e: {}'.format(so))
    