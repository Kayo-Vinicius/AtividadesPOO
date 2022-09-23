salBase = int(input('Informe seu salario: '))
salGratificado = (salBase * 5) / 100
valorImposto = ((salBase + salGratificado) * 7) / 100
salFinal = (salBase + salGratificado) - valorImposto
print('Seu salario final será de %s reais' %salFinal)