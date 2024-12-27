
frase = str(input('Entre com um nome: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range (len(junto) -1, -1, -1): 
    inverso = inverso + junto[letra]
if inverso == junto:
    print('{} ela é um palíndromo !'.format(frase))
else:
    print('{} ela não é um palíndromo'.format(frase))
print('{} e {}'.format(junto, inverso))
    

