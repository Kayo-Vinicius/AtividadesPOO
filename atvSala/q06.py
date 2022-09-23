#Questao 6

maiorNum = 0
menorNum = 0

for i in range(5):
    num = int(input('Digite um numero: '))
        
    if num >= maiorNum:
       maiorNum = num
        
    if menorNum == 0:
        menorNum = maiorNum
       
    if num < maiorNum & menorNum >= num:
        menorNum = num
        
print('Maior: ',maiorNum)
print('Menor: ',menorNum)