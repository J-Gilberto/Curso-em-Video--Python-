from random import randint
from time import sleep

tentativas = 0
pc = randint(1, 10)

while True:
    play = int(input('Digite um número de 1 a 10: '))
    tentativas = tentativas + 1
    if play == pc:
        print('Você acertou!')
        break
    else:
        print('Você errou, tente novamente!')
    sleep(1)
print(f'Você tentou {tentativas} vezes')