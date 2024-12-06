print('{:=^20}'.format ('Programa para calcular condiçoes de pagamento.'))
print('=-='*16)

preço = float(input('entre com o valor do produto R$ '))
print('=-='*16)
av = int(input('entre com o numero de 1 para modalidade Avista, 2 avista no cartao, 3 2X no cartao, 4 3x ou mais no cartao: '))

avista1 = preço * 0.10 
avista2 = preço * 0.05
cartao1 = preço
cartao2 = preço * 0.20
total1 = preço - avista1
total2 = preço - avista2
total3 = preço
total4 = preço + cartao2

if av == 1:
    print('Sua compra vai ficar no valor de R$ {}'.format(total1))
elif av == 2:
    print('Sua compra vai ficar no valor de R$ {}'.format(total2))
elif av == 3:
    print('Sua compra vai ficar no valor de R$ {}'.format(total3))
else:
    print('Sua compra vai ficar no valor de R$ {}'.format(total4))
    
# from random import randint

# print('  Programa de jokempo')
# print('=-='*8)

# jogador = int(input('Entre com 1 = Pedra, 2 = Tesoura, 3 = Papel: '))

# if jogador == 1:
#     print('Jogador entrou com Pedra')
# elif jogador == 2:
#     print('Jogador entrou com Tesoura')
# else:
#     print('Jogador entrou com Papel')
    
# print('=-='*8)  
  
# cpu = randint(1,3)

# if cpu == 1:
#     print('CPU entrou com Pedra')
# elif cpu == 2:
#     print('CPU entrou com Tesoura')
# else:
#     print('CPU entrou com Papel')
    
# print('=-='*8)  
    
# if jogador == cpu:
#     print('Empate')
# elif (jogador == 1 and cpu == 2) or (jogador == 2 and cpu == 3) or (jogador == 3 and cpu == 1 ):
#     print('Jogador ganhou')
# else:
#     print('COU vence')