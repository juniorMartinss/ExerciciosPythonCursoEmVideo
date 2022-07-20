#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúculas.
#O nome com todas as letres minúsculas.
#Quantas letras ao todos (sem considerar espaços)
#Quantas letras tem o primeiro nome.


nc = input('Digite o nome completo: ')
print('O nome em letra maiúscula é: '+ nc.upper())
print('O nome em letra minúscula é: '+ nc.lower())
print('A quantiade de caracteres no nome é: ' , len(nc), 'caracteres')
divi = nc.split()
print('A quantidade de caracteres no primeiro nome é: ' , len(divi[0]), 'caracteres')

