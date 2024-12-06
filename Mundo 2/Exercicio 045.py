# from random import randint

# def entrada_jogador():
#     while True:
#         try:
#             jogador = int(input('Entre com 1 = Pedra, 2 = Tesoura, 3 = Papel: '))
#             if jogador in [1, 2, 3]:
#                 if jogador == 1:
#                     print('Jogador entrou com Pedra')
#                 elif jogador == 2:
#                     print('Jogador entrou com Tesoura')
#                 elif jogador == 3:
#                     print('Jogador entrou com Papel')
#                 return jogador
#             else:
#                 print('Escolha inválida! Por favor, entre com 1, 2 ou 3.')
#         except ValueError:
#             print('Entrada inválida! Por favor, entre com um número inteiro (1, 2 ou 3).')

# def entrada_cpu():
#     cpu = randint(1, 3)
#     if cpu == 1:
#         print('CPU entrou com Pedra')
#     elif cpu == 2:
#         print('CPU entrou com Tesoura')
#     elif cpu == 3:
#         print('CPU entrou com Papel')
#     return cpu

# def determinar_vencedor(jogador, cpu):
#     if jogador == cpu:
#         print('Empate')
#     elif (jogador == 1 and cpu == 2) or (jogador == 2 and cpu == 3) or (jogador == 3 and cpu == 1):
#         print('Jogador ganha')
#     else:
#         print('CPU ganha')

# def jogar_jokenpo():
#     print('  Programa de Jokenpô')
#     print('=-='*8)
    
#     jogador = entrada_jogador()
#     print('=-='*8)
    
#     cpu = entrada_cpu()
#     print('=-='*8)
    
#     determinar_vencedor(jogador, cpu)

# # Chamando a função para jogar Jokenpô
# jogar_jokenpo()




from time import sleep
from random import randint

def entrada_jogador():
    
    while True:
        try:
            play1 = int(input('Entre com: 1 Pedra, 2 Tesoura, 3 Papel '))
            if play1 in [1, 2, 3]:
                if play1 == 1:
                    print('Jogador entrou com Pedra')
                elif play1 == 2:
                    print('Jogador entrou com Tesoura')
                elif play1 == 3:
                    print('Jogador entrou com Papel')
                    
                return play1
            else: 
                print('Porfavor entrar com: 1 Pedra, 2 Tesoura, 3 Papel')
        except ValueError:
            print('entrem com os numeros inteiros, de 1 a 3')
            
def entrada_cpu():
    
    cpu = randint(1, 3)
    if cpu == 1:
        print('CPU entrou com Pedra')
    elif cpu == 2:
        print('CPU entrou com Tesoura')
    elif cpu == 3:
        print('CPU entrou com Papel')
    return cpu

def vencedor(play, cpu):
    if play == cpu:
        print('Ouve Empate')
    elif play (play == 1 and cpu == 2) or (play == 2 and cpu == 3) or (play == 3 and cpu == 1):
        print('Jogador Vence !')
    else:
        print('CPU Vence !')
        
def lutem():
    print('Jokenpo')
    print('=-='*7)
    
    play = entrada_jogador()
    print('=-='*7)
    
    cpu = entrada_cpu()
    print('=-='*7)
    
    vencedor(play, cpu)
    
lutem()
    