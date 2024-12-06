from datetime import date

print('Programa da confederaçao de nataçao')
nasc = int(input('entre com o ano de nascimento do aluno: '))
anos = date.today().year

if anos <=9:
    print('Sua categoria e Mirim, pois sua idade e {} anos'.format(anos))
elif anos <=14:
    print('Sua categoria e Infantil, pois sua idade e {} anos'.format(anos))
elif anos <=19:
    print('Sua categoria e Junior, pois sua idade e {} anos'.format(anos))
elif anos <=20:
    print('Sua categoria e Senior, pois sua idade e {} anos'.format(anos))
else:
    print('Sua categoria e Master, pois sua idade e {} anos'.format(anos))