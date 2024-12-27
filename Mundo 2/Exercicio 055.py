pesoMaior = 0
pesoMenor = 0

for c in range(1, 6):
    peso = float(input(f'Entre com o peso da {c}ª pessoa: '))
    
    if c == 1:  # Na primeira iteração, inicializamos as variáveis.
        pesoMaior = peso
        pesoMenor = peso
    else:  # Nas iterações subsequentes, comparamos e atualizamos as variáveis conforme necessário.
        if peso > pesoMaior:
            pesoMaior = peso
        if peso < pesoMenor:
            pesoMenor = peso

# Exibimos os resultados finais.
print(f'Maior peso: {pesoMaior}')
print(f'Menor peso: {pesoMenor}')


pesoMaior = 0
pesoMenor = 0

for c in range(1,6):
    peso = float(input(f'Entre com o peso do {c}° candidato: '))
    if c == 1:
        pesoMaior = peso
        pesoMenor = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        if peso < pesoMenor:
            pesoMenor = peso
print(f'Este foi o maior peso {pesoMaior}Kg')
print(f'Este foi o menor peso {pesoMenor}Kg')


        
     