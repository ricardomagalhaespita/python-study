# Operadores in e not in

# 0 1 2 3 4 5 6
# R i c a r d 0
# -7-6-5-4-3-2-1


# nome = 'Ricardo'
# print(nome[2])
# print('R' in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')