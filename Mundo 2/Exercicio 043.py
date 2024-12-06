# print('Programa para analizar o seu IMC!')
# print('=-='*11)
# print('=-='*11)
# altura = float(input('Entre com a sua altura: '))
# peso = float(input('Entre com o seu peso '))

# imc = peso / (altura * altura)

# if imc < 18.5:
#     print('Esta abaixo do seu peso ideal, seu IMC e {:.2f}'.format(imc))
# elif imc < 25:
#     print('Esta com o peso ideal, seu IMC e {:.2f}'.format(imc))
# elif imc < 30:
#     print('Esta com sobrepeso, seu IMC e {:.2f}'.format(imc))
# elif imc < 40:
#     print('Esta com obesidade, seu IMC e {:.2f}'.format(imc))
# else:
#     print('Esta com obessidade morbida, procure ajuda! Seu IMC e {:.2f}'.format(imc))

def imc():
    
    peso = float(input('Entre com seu peso: '))
    altura = float(input('Entre com a sua altura: '))
    mul = peso / (altura ** 2)
    
    if mul <= 18.5:
        print('Seu peso e {} Kg, levando em consideraçao a sua altura {} cm, seu IMC {:.1f} esta abaixo do ideal.'.format(peso, altura, mul))
    elif mul <= 25:
        print('Seu peso e {} kg, levando em consideraçao a sua altura {} cm, seu IMC {:.1f} esta com o peso ideal.'.format(peso, altura, mul))
    elif mul <= 30:
        print('Seu peso e {} Kg, levando em consideraçao a sua altura {} cm, seu IMC {:.1f} esta com sobrepeso.'.format(peso, altura, mul))
    elif mul <= 40:
        print('Seu peso e {} Kg, levando em consideraçao a sua altura {} cm, seu IMC {:.1f} esta com obesidade.'.format(peso, altura, mul))
    else:
        print('Seu peso e {} kg, levando em consideraçao a sua altura {} cm, seu IMC {:.1f} esta com obesidade morbida.'.format(peso, altura, mul))
    return imc

imc()
    



