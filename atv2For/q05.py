#Questao 5

num = int(input('Digite um numero: '))
f1 = 0
n1 = 0
n2 = 1
aux = 0

f1 = n1 + n2
print(n1,f1, end=" ")

while (num >= aux):
    
    aux = f1 + n1
    n1 = f1
    f1 = aux
    print(aux, end=" ")