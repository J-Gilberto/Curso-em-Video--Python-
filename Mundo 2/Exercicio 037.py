print('Programa de conversao de numeros interios para Binarios, Octal e Hexadecimal')
entrada = int(input('Entre com um valor inteiro: '))
precione = int(input('Digite 1 para Binario, Digite 2 para Octal, Digite 3 para Hexadecimal:  '))
binario = bin(entrada)
octal = oct(entrada)
hexadecimal = hex(entrada)

if precione == 1:
    print('Seu valor de entrada foi de {} ele transformado em Binario e: {}'.format(entrada,binario[2:]))
elif precione == 2:
     print('Seu valor de entrada foi de {} ele transformado em Octal e: {}'.format(entrada,octal[2:]))
elif precione == 3:
    print('Seu numero de entrada foi de {} ele transformado em BHexadecimal e: {}'.format(entrada,hexadecimal[2:])) 
    