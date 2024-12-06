from time import sleep

soma = 0
print('Programa de calcular numeros Pares !')
for numero in range(0, 6):
    num = int(input('Entre com numeros inteiros: '))
    print('=-='*10)
    if num % 2 == 0:
        soma = soma + num
sleep(5)
print(soma)