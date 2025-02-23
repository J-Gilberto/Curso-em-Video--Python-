# soma = 0

# while True:
#     Entrada = int(input('Entre com um número: '))
#     if Entrada == 999:
#         break
#     soma = soma + Entrada
# print(f'A soma dos números é: {soma}')


soma = 0
cont = 0

while True:
    entrada = int(input(f'Entre com um número: '))
    if entrada == 999:
        break
    soma = soma + entrada
    cont = cont + 1
print(f'você digitou {cont} números e o total é {soma}')
