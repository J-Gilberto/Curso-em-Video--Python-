
# print('Programa para Media do Aluno.')
# ent = input('Entre com as notas separadas por espaco: ')

# numero = list(map(float, ent.split()))
# soma = sum(numero)
# media = soma / len(numero)

# if media < 5:
#     print('Voce foi reprovado, sua media foi de {:.2f}'.format(media))
# elif media > 5 and media < 6.9 :
#     print('Voce esta em recuperaçao, sua media foi de {:.2f}'.format(media))
# elif media > 7:
#     print('Voce esta aprovado, meus parabens, sua media foi de {:.2f}'.format(media))
# print('Bons estudos !')


entrada1 = float(input('Entre com sua primeira nota: '))
entrada2 = float(input('Entre com sua segunda nota: '))
entrada3 = float(input('Entre com sua terceira nota: '))

nota = (entrada1 + entrada2 + entrada3) / 3

if nota <= 5:
    print('Sua media foi de {:.1f} voce esta reprovado !'.format(nota))
elif nota <= 6.9:
    print('Sua media foi de {:.1f} voce esta em recuperaçao !'.format(nota))
else:
    print('Sua media foi de {:.1f} voce esta aprovado !'.format(nota))
    