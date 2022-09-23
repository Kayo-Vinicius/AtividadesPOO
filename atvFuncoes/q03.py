#Questao 3

def volEsfera(raio):
    return (4 * 3.14 * raio**3)/3
    
raio = int(input("Digite o raio: "))

print("O volume da esfera é:", volEsfera(raio))