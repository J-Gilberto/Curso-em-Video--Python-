print('Programa para analizar triangulos')
print('=-='*50)
print('=-='*50)

a = input('Entre com os segmento A: ')
b = input('Entre com os segmento B: ')
c = input('Entre com os segmento C: ')

def tringulo(lados):
    a, b, c = lados
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
def tip_triangulo(lados):
    a, b, c = lados
    if a == b == c:
        return 'Equilatero'
    elif a == b or a == c or b == c:
        return 'Isosceles'
    else:
        return 'Escaleno'
    
lados = (a, b, c)
if tringulo(lados):
    print('Os segmentos formam um triangulo {}'.format(tip_triangulo(lados)))
else:
    print('Os segmentos nao formam um triangulo')
