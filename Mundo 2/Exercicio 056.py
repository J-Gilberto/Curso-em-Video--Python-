# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
# A média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

# maior = 0
# name = ''
# total = 0
# media = 0
# totMulher = 0

# for c in range(1, 5):
    
#     nome = str(input(f'Entre com o nome da {c}° pessoa: ')).strip()
#     idade = int(input(f'Entre com a idade: '))
#     sexo = str(input('Entre com M para masculino e F para feminino: ')).strip()
#     print('=-='*10)
#     total = total + idade
    
#     if c == 1 and sexo in 'Mm':
#         maior = idade
#         name = nome
#     if sexo in 'Mm' and idade > maior:
#         maior = idade
#         name = nome
#     if sexo in 'Ff' and idade < 20:
#         totMulher = totMulher + 1      
        
# media = total / 4  
# print(f'Idade media do grupo foi de {media} anos')
# print(f'O homem mais velho do grupo se chama {name} e tem {maior} anos')
# print(f'Ao todo existem {totMulher} mulheres com idade abaixo de 20 anos')



# media = 0
# total = 0
# maior = 0
# new = ''
# totMul = 0
# for p in range(1,5):
#     print('=-='*10)
#     nome = str(input(f'Entre com o nome do {p} candidato: ')).strip()
#     idade = int(input('Entre com a idade: '))
#     sexo = str(input('Entre com o sexo M/F: ')).strip()
#     total = total + idade  # como seram 4 entradas, estou totalizando elas com a expressão 'total = total + idade' tambem tenho que usar o valor de soma que é 'Total = 0'
#     media = total / 4 # aqui tambem uso a soma 'Media = 0' por que ele vai dividir o total por 4 vezes como esta na expressão
    
#     if p == 1 and sexo in 'Mm': # como não tem referencia, estamos usando a primeira entrada pra ser a maior idade "p==1" e tambem "sexo in 'Mm'" para toda vez que entrar o sexo masculino. 
#         maior = idade # aqui ele vai guardar o valor do maior que seria a entrada e armazenar em "maior=0", aqui o maior recebe idade e o guarda como referencia, ate outro maior aparecer.
#         new = nome # aqui a mesma coisa, ele vai guardar tanto a idade como o nome foi apontado la em cima, então o p==1 quando ele receber a idade e nome do "homem" mais velho.
        
#     if sexo in 'Mm' and idade > maior: # neste aspecto aqui, "sexo in 'Mm'" quando entrar sexo masculino ele vai ver se a idade é maior que o valor "maior = 0" que foi armazenado antes.
#         maior = idade # aqui ele vai guardar o valor do maior que seria a entrada e armazenar em "maior=0", aqui o maior recebe idade e o guarda como referencia, ate outro maior aparecer.
#         new = nome # aqui a mesma coisa, ele vai guardar tanto a idade como o nome foi apontado la em cima, então o p==1 quando ele receber a idade e nome do "homem" mais velho.
    
#     if sexo in 'Ff' and idade < 20:
#         totMul = totMul + 1
        
# print(media)
# print(f'idade {maior}, nome {new}')
# print(f'Total de mulheres foi {totMul}')


















# m = 0
# t = 0
# for i in range(1,5):
#     idade = int(input('Entre com a idade: '))
#     t = t + idade
#     m = t / 4
# print(m)


# tot = 0
# med = 0   
# for p in range(1,5):
#     id = int(input('entre com a idade: '))
#     tot = tot + id
#     med = tot / p
# print(med)
    
maioridade = 0
media = 0
idade = 0
nome = ''
totalMulher = 0

for p in range(1,5):
    print('')

