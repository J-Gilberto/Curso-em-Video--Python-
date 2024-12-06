from time import sleep

primeiro = int(input('Primeiro elemento: '))
razao = int(input('Entre com a Razao:'))
n = int(input('Quantos elementos exibir: '))

final = primeiro + (n - 1)*razao
final = final + 1


for cont in range(primeiro, final, razao):
    print (cont)