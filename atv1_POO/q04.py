nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))

if (nota1 < 0 or nota1 > 10): 
    print('Nota invalida') 
elif (nota2 < 0 or nota2 > 10):
    print('Nota invalida')
else:
    media = (nota1 + nota2) / 2
    print('Sua media é',media)
  