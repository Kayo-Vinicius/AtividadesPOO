valorProduto = int(input('Informe o valor do produto: '))
desconto = (valorProduto * 10) / 100
valorFinal = valorProduto - desconto
print('Voce pagara %s reais' %valorFinal)

parcela = valorProduto / 3
print('Voce para %s reais todo mes por parcela' %parcela)

comissaoVista = (valorFinal * 5) /100
print('O vendedor rebera %s reais de comissao se a venda for a vista' %comissaoVista)

comissaoParcelada = (valorProduto * 5) / 100
print('O vendedor recebera %s reais de comissao se a venda for parcelada' %comissaoParcelada)