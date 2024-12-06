print('Programa para financiamento da sua casa propria!')
valor = int(input('Entre com o valor da casa que deseja: R$ '))
salario = float(input('Informe o seu salario: R$ '))
dividido = int(input('Quantas anos pretende dividir esta casa: '))

anos = dividido*12
val01 = valor/anos
val02 = (30/100)*salario

if val01 <= val02:
    print('Parabens sua casa propria foi aprovada, o valor da prestaçao fica R${:.2f} baseado no seu salario R${:.2f}'.format(val02,salario))
else:
    print('Sinto muito sua casa propria nao foi aprovada, o valor da prestaçao fica R${:.2f} baseado no seu salario R${:.2f}'.format(val02,salario))
