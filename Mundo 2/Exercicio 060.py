n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print(f'O fatorial é: {f}')