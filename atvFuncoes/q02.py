#Questao 2

def verificaPositivo(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    elif num == 0:
        return 0

n = int(input("Digite um numero: "))

print(verificaPositivo(n))
