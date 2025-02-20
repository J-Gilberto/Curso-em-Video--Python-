# while True:
    
#     opção = int(input('''
#     [1] Soma
#     [2] Multiplicação
#     [3] Maior
#     [4] Novos números
#     [5] Sair
#     '''))
#     if opção == 1:
#         número01 = int(input('Digite o primeiro número: '))
#         número02 = int(input('Digite o segundo número: '))
#         print(f'A soma dos números {número01} e {número02} é: {número01 + número02}')
#     elif opção == 2:
#         número01 = int(input('Digite o primeiro número: '))
#         número02 = int(input('Digite o segundo número: '))
#         print(f'A multiplicação dos números {número01} e {número02} é: {número01 * número02}')
#     elif opção == 3:
#         número01 = int(input('Digite o primeiro número: '))
#         número02 = int(input('Digite o segundo número: '))
#         if número01 > número02:
#             print(f'O número {número01} é maior que o número {número02}')
#         elif número01 < número02:
#             print(f'O número {número02} é maior que o número {número01}')
#         else:
#             print('Os números são iguais')
#     elif opção == 4:
#         print('Digite novos números')
#     elif opção == 5:    
#         break
    
# num01 = int(input('Entre com primeiro número inteiro: '))  
# num02 = int(input('Entre com segundo número inteiro: ')) 
# print('=-='*15) 

# while True:

#     entrada = int(input('''Entre com devido numero para:
# [1] Multiplicaçao
# [2] Soma
# [3] Maior
# [4] Novos números
# [5] Sair do programa
#         '''))
    
#     if entrada == 1: 
#         t1 = num01 * num02
#         print(f'Os numeros {num01} X {num02} é igual a: {t1}')
#         print('=-='*15)
#     elif entrada == 2:
#         t2 = num01 + num02
#         print(f'Os numeros {num01} + {num02} é igual a: {t2}')
#         print('=-='*15)
#     elif entrada == 3:
#         if num01 > num02:
#             print(f'Entrada 1 {num01} é maior que Entrada 2 {num02}')
#             print('=-='*15)
#         elif num01 < num02:
#             print(f'Entrada 2 {num02} é maior que Entrada 1 {num01}')
#             print('=-='*15)
#         elif entrada == 4:
#             print(f'Entre com novos valores:')
#             num01 = int(input('Entre com primeiro número inteiro: '))  
#             num02 = int(input('Entre com segundo número inteiro: ')) 
#         else:
#             print(f'Entrada 1 {num02} é igual a Entrada 2 {num01}')
#             print('=-='*15)
#     elif entrada == 5:
#         break
        
n1 = int(input('Entre com o primeiro valor: '))
n2 = int(input('Entre com o segundo valor: '))
print('=-='*15)

while True:
    
    entrada = int(input('''Entre com devido numero para:
    [1] Somar 
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    sua opção foi: ''' ))     
    
    if entrada == 1:
        print(f'Você escolheu Somar:')  
        soma = n1 + n2
        print(f'A soma de {n1} com {n2} da igual a: {soma}')
        print('=-='*15)
    elif entrada == 2:
        print(f'Você escolheu Multiplicar: ')
        mult = n1 * n2
        print(f'A Multiplicação de {n1} com {n2} da igual a: {soma}')
        print('=-='*15)
    elif entrada == 3:
        print(f'Você escolheu qual seria o Maior:')
        if n1 > n2:
            print(f'O primeiro valor {n1} é maior')
        elif n1 < n2:
            print(f'O segundo valor {n2} é maior')
        else:
            print(f'Tanto o primeiro valor {n1} como o segundo valor {n2} são iguais.')
    elif entrada == 4:
        print(f'Informe os números novamente: ')
        n1 = int(input(f'Entre com o primeiro valor: '))
        n2 = int(input(f'Entre com o segundo valor: '))
    elif entrada == 5:
        break
    else:
        print(f'Entre com uma opção valida!')
    print(f'=-='*15)
print(f'Fim do programa !')