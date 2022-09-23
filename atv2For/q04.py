#Questao 4

import math

num = int(input('Digite um numero entre 100 e 999: '))

while (num <= 100 or num > 999):
    num = int(input('Digite um numero entre 100 e 999: '))

centena = num/100
dezena = num%100
unidade = dezena%10
dezena = dezena/10

print('Centena: {}'.format(math.trunc(centena)))
print('Dezena: {}'.format(math.trunc(dezena)))
print('Unidade: {}'.format(unidade))