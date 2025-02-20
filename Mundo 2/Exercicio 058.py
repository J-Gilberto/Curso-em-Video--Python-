# from random import randint
# from time import sleep

# tentativas = 0
# pc = randint(1, 10)

# while True:
#     play = int(input('Digite um número de 1 a 10: '))
#     tentativas = tentativas + 1
#     if play == pc:
#         print('Você acertou!')
#         break
#     else:
#         print('Você errou, tente novamente!')
#     sleep(1)
# print(f'Você tentou {tentativas} vezes')


# from random import randint


# tentativas = 0
# pc = randint(1,10)

# while True:
#     play = int(input(f'Entre com seu número: '))
#     tentativas = tentativas + 1
#     if play == pc:
#         print(f'Jogador venceu com o número {play}')
#         break
#     elif play != pc:
#         print(f'Tente novamente!')
# print(f'Você venceu parabens, seu numero de tentativas foi {tentativas}')
        
from random import randint

tentativas = 0
pc = randint(1,10)

while True:
    jogador = int(input(f'Entre cm um numero entre 1 a 10: '))
    tentativas = tentativas +1
    if jogador == pc:
        print(f'Jogador venceu com o número: {jogador}')
        break
    elif jogador != pc:
        print(f'Tente novamenten !')
print(f'Você venceu, meus parabens foram {tentativas} tentativas para um unico acerto!')