
soma = 0
for cont in range(1,503, 2 ):
    if cont % 3 == 0:
        soma = soma + cont
        print(cont)
print(soma)

soma = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        print(c, end=' .')
print (soma)


s = 0
c = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        c = c  + 1
        s = s + n 
        print(n, end=' .')
print('Valores encontrados foi de {} e a soma de todos eles e: {}'.format(c, s))


z = 0
l = 0
for m in range(1, 501, 2):
    if m % 3 == 0:
        z = z + m
        l = l + 1
        print(m, end=' .')
print('Vezez multplicado {} e total: {}'.format(l, z))


from time import sleep

conts = 0
somas = 0
for contador in range(1, 501, 2):
    if contador % 3 == 0:
        somas = somas + contador
        conts = conts + 1
        sleep(0.5)
        print(contador)
print('quantidade multiplicado {} e sua soma {}'.format(conts, somas))       