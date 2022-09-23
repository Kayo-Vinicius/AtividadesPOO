#Questao 5

def volCilindro(alt, raio):
    return 3.14 * raio**2 * alt
    
altura = int(input("Digite a altura: "))
raio = int(input("Digite o raio: "))

print("O volume do cilindro é: ", volCilindro(altura, raio))