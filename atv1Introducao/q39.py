premioTotal = 780.00000

premio1 = (premioTotal * 46) / 100
print('O primeiro ganhador recebera %s de dinheiro' %premio1)

premio2 = (premioTotal * 32) / 100
print('O segundo ganhador recebera %s de dinheiro' %premio2)

premio3 = premioTotal - (premio1 + premio2)
print('O terceiro ganhador recebera %s de dinheiro' %premio3)