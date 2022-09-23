num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

if (num1 > num2):
    print('%s é maior'%num1)
    difenca = num1 - num2
    print('Essa é a diferença entre eles: ',difenca)
if (num2 > num1):
    print('%s é maior'%num2)
    difenca = num2 - num1
    print('Essa é a diferença entre eles: ',difenca)
if (num1 == num2):
    print('Os dois numeros sao iguais')