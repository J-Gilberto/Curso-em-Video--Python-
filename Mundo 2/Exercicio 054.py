from time import  sleep
from datetime import date

maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input(f'Entre com a ano de nascimento do {c}° cadetes: '))
    atual = date.today().year
    idade = atual - nasc
    if idade >= 18:
        maior = maior + 1
        # print(f'Usuario com {idade} anos é maior de idade!')
    else:
        menor = menor + 1
        # print(f'Usuario com {idade} anos é menor de idade!')
sleep(2)
print(f'total de {maior} maiores de idade !')
print(f'total de {menor} menores de idade !')
    

from datetime import date

maior = 0
menor = 0

for cont in range(1, 8):
    nasc = int(input('Entre com o ano de nascimento: '))
    ano = date.today().year
    idade = ano - nasc
    
    if idade > 18:
        maior = maior + 1
        print(f"este individou tem {idade} anos, então é maior de idade. ")
    else:
        menor = menor + 1
        print(f'este individou tem {idade} anos, então é menor de idade. ')
print(f'Existem {maior} maiores de idade.')
print(f'Existem {menor} menores de idade.')


from datetime import date

maior = 0
menor = 0

for c in range(1, 8):
    nasc = int(input(f'Entre com a data de nascimento do {c}° cadete: '))
    
    ano = date.today().year
    idade = ano - nasc
    
    if idade > 18:
        maior = maior + 1
    else:
        menor = menor + 1
print(f'Existem {maior} maiores de idade !')
print(f'Existem {menor} menores de idade !')
    