from time import sleep

print('=-='*7)
num = int(input('Entre com um valor de 1 a 10: '))
print('=-='*7)
for numero in range(0, 11):
    mult = numero * num
    print('{} x {} = {}'.format(num, numero, mult))
    print('=-='*3)
    sleep(1)
print('Fim do programa !')

from time import sleep

cont = int(input('Entre com um numero inteiro: '))
for c in range(0, 11):
    multi = c * cont
    sleep(0.5)
    print('{} x {} = {}'.format(cont, c, multi))
print('Fim')


from time import sleep

n =  int(input('Entre com um valor: ')) 
for x in range (0, 11):
    total = n * x
   
    print('{} x {} = {}'.format(n, x, total))
print('Fim')


from time import sleep

laço = int(input('entre com um valor inteiro: '))
for todes in range(0, 11):
    print('{} X {} = {}'.format(laço, todes, laço*todes))