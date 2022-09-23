#Questao 3

maiorNum = 0
qtdLida = 0

i = int(input('Informe quantos numeros ira digitar: '))

for i in range(i):
    num = int(input('Digite um numero: '))
        
    if num >= maiorNum:
       maiorNum = num
       qtdLida = qtdLida + 1
        
print('Maior: ',maiorNum)
print('Lida: ', qtdLida)
