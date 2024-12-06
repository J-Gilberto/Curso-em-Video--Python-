from datetime import date

print('Programa de alistamento militar (O cancer do Brasil democratico)')
id = int(input('Entre com o ano do seu nascimento: '))

ano = date.today().year
anos = ano - id
menos = 18 - anos
mais = anos - 18

if anos == 18:
    print('Voce esta apto para o alistamento militar! sua idade {} anos.'.format(anos))
elif anos < 18:
    print('Voce ainda nao esta apto para o alistamento militar (Sorte), sua idade e {} anos, ainda falta {} anos para o seu alistamento.'.format(anos, menos))
elif anos > 18:
    print('Voce passou do prazo de alistamento, compareça mais breve possivel a um guartel militar para resolver esta questao, sua idade e {} anos, ja se passaram {} anos da sua inscriçao obrigatoria.'.format(anos, mais))
    