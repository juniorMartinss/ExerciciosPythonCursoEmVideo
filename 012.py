#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

val = float(input('Digite o valor do produto: '))
nval = val * 0.05
desc = val - nval
print('O novo valor do produto que era {}, acresentando 5% é: {}'.format(val, desc))