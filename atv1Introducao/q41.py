horaTrabalhada = int(input('Informe quantas horas trabalhou no mês: '))
valorHora = int(input('Informe o valor da hora trabalhada: '))
salBruto = ((horaTrabalhada * valorHora) * 10) / 100
salLiquido = (horaTrabalhada * valorHora) + salBruto
print('Seu salario foi de %s reais' %salLiquido)