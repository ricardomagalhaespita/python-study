nome = 'Ricardo Magalhães Pita'
altura = 1.80
peso = 90
imc = peso / (altura * altura)

# Utilizando F-strings
linha_1 = f'{nome} possui {peso}, KG com uma altura de {altura:.2f}.'
linha_2 = f'Seu IMC é de: {imc}'

print(linha_1)
print(linha_2)

