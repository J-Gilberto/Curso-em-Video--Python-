soma = 0

while True:
    Entrada = int(input('Entre com um número: '))
    if Entrada == 999:
        break
    soma = soma + Entrada
print(f'A soma dos números é: {soma}')