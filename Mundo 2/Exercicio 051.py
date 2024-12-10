from time import sleep

primeiro = int(input('Primeiro elemento: '))
razao = int(input('Entre com a Razao:'))
n = int(input('Quantos elementos exibir: '))

final = primeiro + (n - 1)*razao
final = final + 1


for cont in range(primeiro, final, razao):
    print (cont)
    
    
pri = int(input('Entre com o Primeiro termo: '))
raz = int(input('Entre com a Razao: ')) 
decimo = pri + (11 - 1) * raz
for c in range (pri, decimo, raz):
    print('{}'.format(c, end= ' >'))
print('fim')



ent = int(input('Entre com o primeiro termo: '))
rosa = int(input('Entre com a razao: '))
dez = ent + (11 - 1) * rosa
for cc in range(ent, dez, rosa):
    print('{}'.format(cc))
print('Fim')





primeiro_termo = int(input('Entre com o primeiro termo: '))
a_razao = int(input('Entre com a Razao: '))
decimo_01 = primeiro_termo + (11 - 1) * a_razao

for contator in range(primeiro_termo, decimo_01, a_razao):
    print('{}'.format(contator))
print('Fim!')
