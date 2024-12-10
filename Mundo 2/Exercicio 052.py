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
        
    
