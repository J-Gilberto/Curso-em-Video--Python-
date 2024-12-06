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
