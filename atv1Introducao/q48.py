qtdSegundos = int(input('Informe a quantidade de segundos: '))
horas = qtdSegundos // 3600
segRestou = qtdSegundos % 3600
minutos = segRestou // 60
segundos = segRestou % 60

print('%sh'%horas)
print('%sm'%minutos)
print('%ss'%segundos)