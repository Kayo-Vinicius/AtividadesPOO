class Cliente():
    def __init__(self, nome_pessoa, cpf_pessoa) -> None:
        self.nome = nome_pessoa
        self.cpf = cpf_pessoa
    
class Conta_Bancaria(Cliente):
    def __init__(self, nome, cpf, numero_conta, saldo_conta) -> None:
        self.numConta = numero_conta
        self.saldo = saldo_conta
        self.contas_bancarias = []
        self.nome = nome
        self.cpf = cpf

    def criarConta(self, nome, cpf, numero_conta, saldo_conta):
        self.contas_bancarias.append(Conta_Bancaria(nome, cpf, numero_conta, saldo_conta))

    def imprimirContas(self):
        for busca in self.contas_bancarias: 
            print(busca.nome, busca.cpf , busca.numConta, busca.saldo)


class Conta_Corrente(Conta_Bancaria):
    def transferencia(self, numero_conta, valor_transferencia):
        taxa_transferencia = 2
        for busca in self.contas_bancarias:
            if busca.numConta == numero_conta:
                    print(f'Saldo Antes:{busca.numConta} {busca.saldo}')
                    taxa_transferencia *= 5
                    busca.saldo = busca.saldo - (valor_transferencia + taxa_transferencia)
                    print(f'Saldo Depois:{busca.numConta} {busca.saldo}')

class Conta_Poupanca(Conta_Bancaria):
    def transferencia(self, numero_conta, valor_transferencia):
        taxa_transferencia = 2
        for busca in self.contas_bancarias:
            if busca.numConta == numero_conta:
                    taxa_transferencia *= 0.25
                    print(f'Saldo Antes:{busca.numConta} {busca.saldo}')
                    busca.saldo = busca.saldo - (valor_transferencia + taxa_transferencia)
                    print(f'Saldo Depois:{busca.numConta} {busca.saldo}')
    

c1 = Conta_Corrente('kayo', '1111', 123, 1000)
c1.criarConta('kayo', '1111', 123, 1000)
c1.imprimirContas()
c1.transferencia(123, 100)


c2 = Conta_Poupanca('bia', '2222', 456, 2000)
c2.criarConta('bia', '2222', 456, 2000)
c2.imprimirContas()
c2.transferencia(456, 200)