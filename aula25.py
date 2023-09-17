
# Interpolação basica de strings
# s - string 
# d/i - int 
# f - float 
# x/X - hEXADECIMAL(abcdef01234567)

nome = 'Ricardo'
preco = 1000.2345
variavel = '%s, o preço total é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))