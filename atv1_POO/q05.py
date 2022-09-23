salario = float(input('Informe seu salrio: '))
prestacao = float(input('Informe o valor da prestação do emprestimo: '))
emprestimo = (salario * 20) / 100

if (prestacao > emprestimo):
    print('Emprestimo não concedido')
else: 
    print('Emprestimo concedido')