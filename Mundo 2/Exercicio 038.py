print('programa de comparaçao numerica')
ent01 = int(input('Entre com o primeiro valor: '))
ent02 = int(input('Entre com o segundo valor: '))

if ent01 > ent02:
    print('O primeiro valor {} e maior que o segundo'.format(ent01))
elif ent01 < ent02:
    print('O segundo valor {} e maior que o primeiro'.format(ent02))
elif ent01 == ent02:
    print('Ambos os valores {} e {} sao iguais.'.format(ent01, ent02))
    