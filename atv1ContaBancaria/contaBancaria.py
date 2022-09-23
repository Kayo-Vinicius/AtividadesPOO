contasCadastradas = []
opcoesMenu = None

def criarConta(numeroConta, nomeCliente, saldoConta):
   novaConta = {'numero': numeroConta, 'usuario': nomeCliente, 'saldo': saldoConta}
   print('Conta criada com sucesso')
   return novaConta

def buscarConta(numeroConta):
   for busca in contasCadastradas:
      if busca['numero'] == numeroConta:
         print('Conta encontrada')
         return busca
      elif busca['numero'] != numeroConta:
         print('Conta não encontrada digite novamente')
         numeroConta = int(input('Numero da conta: '))
         return buscarConta(numeroConta)

def excluirConta(numeroConta):
   for busca in contasCadastradas:
      if busca['numero'] == numeroConta:
         contasCadastradas.remove(busca)
         print('Conta removida')

def transferirValor(pagamento, numContaPaga, numContaRecebe):
   for busca in contasCadastradas:
      if numContaPaga == numContaRecebe:
         print('\n transferencia nao realizada\nObs: Voce nao pode transferir para você mesmo')
      else:  
         if busca['numero'] == numContaPaga:
            saldoContaPaga = busca['saldo']
            if saldoContaPaga <= 0:
               print('Saldo insuficiente')
            else:
               print(f'Saldo antes da transferencia : {saldoContaPaga}')
               saldoContaPaga -= pagamento
               print(f'Saldo depois da transferencia: {saldoContaPaga}')
            if busca['numero'] == numContaRecebe:
               saldoContaRecebe = busca['saldo']
               print(f'Saldo antes da transferencia: {saldoContaRecebe}')
               saldoContaRecebe += pagamento
               print(f'Saldo depois da transferencia: {saldoContaRecebe}')

def verSaldo(numeroConta):
   for busca in contasCadastradas:
      if busca['numero'] == numeroConta:
         print('Seu saldo atual: ', busca['saldo'])

def depositar(numeroConta, valorDeposito):
   for busca in contasCadastradas:
      if busca['numero'] == numeroConta:
         saldoConta = busca['saldo']
   print(f'Saldo antes da transferencia: {saldoConta}')
   saldoConta += valorDeposito
   print(f'Saldo depois da transferencia: {saldoConta}')

while(opcoesMenu != 0):
   print('\n1 - Criar Conta\n2 - Buscar Conta\n0 - Sair')
   opcoesMenu = int(input('Digite o numero da opcão que deseja fazer: '))
   
   if opcoesMenu == 1:
      numeroConta = int(input('Numero da conta: '))
      nomeCliente = input('Nome: ')
      saldoConta = float(input('Saldo: '))
      contasCadastradas.append(criarConta(numeroConta, nomeCliente, saldoConta))

   elif opcoesMenu == 2:
      numeroConta = int(input('Numero da conta: '))
      buscarConta(numeroConta)

      print('\n3 - Excluir Conta\n4 - Realizar Transferência\n5 - Exibir Saldo\n6 - Depositar')
      opcoesMenu = int(input('Digite o numero da opcão que deseja fazer: '))
   
      if opcoesMenu == 3:
         numeroConta = int(input('Numero da conta: '))
         excluirConta(numeroConta)

      elif opcoesMenu == 4:
         print('Informe o numero da conta que vai transferir')
         numContaPaga = int(input('Numero da conta: '))

         print('Informe o numero da conta que vai receber')
         numContaRecebe = int(input('Numero da conta: '))
         valorTrasferencia = float(input('Digite o valor da transferencia: '))
         transferirValor(valorTrasferencia, numContaPaga, numContaRecebe)

      elif opcoesMenu == 5:
         numeroConta = int(input('Numero da conta: '))
         verSaldo(numeroConta)
      
      elif opcoesMenu == 6:
         numeroConta = int(input('Numero da conta: '))
         valorDeposito = float(input('Valor do deposito: '))
         depositar(numeroConta, valorDeposito)