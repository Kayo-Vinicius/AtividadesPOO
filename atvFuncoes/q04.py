#Questao 4

def numMaior(num1, num2):
    if num1 > num2:
        print(f'Maior: {num1}')
    elif num2 > num1:
        print(f'Maior: {num2}')
    elif num1 == num2:
        print('Os numeros sao iguais')
    
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

numMaior(n1, n2)