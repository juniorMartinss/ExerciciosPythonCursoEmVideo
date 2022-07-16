#Crie um programa que leia um número REAL e mostre na tela a sua porção INTEIRA - EX: 6.127 -> 6

import math
n = float(input('Digite um número com ponto: '))
r = math.floor(n)
print('O número digitado foi {} e o número real é {}'.format(n, r))
