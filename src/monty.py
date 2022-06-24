from random import choice

sequencia = ['a', 'b', 'c']
ganhou = 0
perdeu = 0
vitória = 0
derrota = 0

print('\033[01;34mSIMULAÇÃO MONTY HALL\033[m')

#escolha da porta premiada, da porta escolhida pelo competidor e da porta aberta pelo apresentador
# chose the prized door, from the door chosed by the user and the door opened by the holst 

for c in range(1, 1000):
    carro = choice(sequencia)
    escolha = choice(sequencia)
    remover = carro
    while remover == carro or remover == escolha:
        remover = choice(sequencia)

#troca de portas
#change door

    troca = choice(sequencia)
    while troca == remover or troca == escolha:
        troca = choice(sequencia)

    escolha = choice(sequencia)
    while escolha == remover:
        escolha = choice(sequencia)

#contabilizando as vitórias e derrotas
#couting wins and loses 

    if troca == carro:
        ganhou += 1
    else:
        perdeu += 1

    if escolha == carro:
        vitória += 1
    else:
        derrota += 1

#exibindo resultados
#show results 

print('\n\033[01;32mCom a troca:\033[m ')
print(f'Ganhou: {ganhou}\nPerdeu: {perdeu}')

print('\n\033[01;31mSem a troca:\033[m ')
print(f'Ganhou: {vitória}\nPerdeu: {derrota}')



