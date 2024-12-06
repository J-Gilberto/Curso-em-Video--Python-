nome = str(input('Entre com o seu nome: '))
if nome == 'Gilberto':
    print('Bom dia senhor {}, seu nome e mais que lindo!'.format(nome))
elif nome == 'Joao' or 'Tania' or 'Severino' or 'Ismael':
    print('Bom dia senhor {}, sua pessoa e agradavel como um sonho'.format(nome))
else:
    print('Bom dia {}, como posso lhe ajudar?'.format(nome))
print('Volte sempre!')