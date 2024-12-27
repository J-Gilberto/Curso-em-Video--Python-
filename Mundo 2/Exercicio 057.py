while True:
    sexo = str(input('Entre com o seu sexo [M/F]: ')).strip().upper()[0]
    
    if sexo == 'M':
        print('Sexo Masculino')
        break
    elif sexo == 'F':
        print('Sexo Feminino')
        break
    else:
        print('Entre com o sexo correto!')