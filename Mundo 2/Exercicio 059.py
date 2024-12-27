while True:
    
    opção = int(input('''
    [1] Soma
    [2] Multiplicação
    [3] Maior
    [4] Novos números
    [5] Sair
    '''))
    if opção == 1:
        número01 = int(input('Digite o primeiro número: '))
        número02 = int(input('Digite o segundo número: '))
        print(f'A soma dos números {número01} e {número02} é: {número01 + número02}')
    elif opção == 2:
        número01 = int(input('Digite o primeiro número: '))
        número02 = int(input('Digite o segundo número: '))
        print(f'A multiplicação dos números {número01} e {número02} é: {número01 * número02}')
    elif opção == 3:
        número01 = int(input('Digite o primeiro número: '))
        número02 = int(input('Digite o segundo número: '))
        if número01 > número02:
            print(f'O número {número01} é maior que o número {número02}')
        elif número01 < número02:
            print(f'O número {número02} é maior que o número {número01}')
        else:
            print('Os números são iguais')
    elif opção == 4:
        print('Digite novos números')
    elif opção == 5:    
        break
    
    

    