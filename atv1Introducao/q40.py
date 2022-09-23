diasTrabalhados = int(input('Quantos dias trabalhou?'))
salBruto = diasTrabalhados * 30
valorDescontado = (salBruto * 8) / 100
salLiquido = salBruto - valorDescontado
print('Seu salario no final do mês é %s reais' %salLiquido)