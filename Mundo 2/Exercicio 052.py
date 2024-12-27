n = int(input("Verificar numeros primos ate: "))
mult=0

for count in range(1, n + 1):
    if (n % count == 0):
        print("Múltiplo de",count)
        mult = mult + 1

if(mult==0):
    print("É primo")
else:
    print("Tem",mult," múltiplos acima de 2 e abaixo de",n)
    
    
ent = int(input('Entre com numero inteiro: '))
m = 0
for cont in range (1, ent + 1):
    if ent % cont == 0:
        print('Multiplo de', cont, end=' - ')
        m = m + 1
if mult == 0:
    print('Numero primo.')
else:
    print('Este numero nao e primo.')
        
    

num = int(input('Entre com um valor inteiro: '))
soma = 0
tot = 0
for c in range(1, num +1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot = tot + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO Número {} foi divisivel {} Vezes'.format(num, tot, end= ''))
if tot == 2:
    print('{} é Primo !'.format(num))      
else:
    print('{} não é Primo'.format(num))
