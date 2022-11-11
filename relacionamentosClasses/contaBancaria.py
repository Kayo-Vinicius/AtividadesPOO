from multiprocessing.connection import Client


contas_bancarias = []


class Cliente:
    def __init__(self, nome_cliente: str, cpf_cliente: str) -> None:
        self.nome_cliente = nome_cliente
        self.cpf_cliente = cpf_cliente


class Contato:
    def __init__(self, telefone_contato: str) -> None:
        self.telefone_contato = telefone_contato

    def set_clienteBanco(self, cliente: Cliente):
        self.cliente = cliente

    def get_clienteBanco(self):
        return self.cliente

    def dadosContato(self):
        print(
            f'Nome: {self.cliente.nome_cliente} Contato: {self.telefone_contato}')


class Pix:
    def __init__(self, chave_pix: str) -> None:
        self.chave_pix = chave_pix

    def set_clienteBanco(self, cliente: Cliente):
        self.cliente = cliente

    def get_clienteBanco(self):
        return self.cliente

    def dadosCliente(self):
        print(
            f'Nome: {self.cliente.nome_cliente} CPF: {self.cliente.cpf_cliente} Chave Pix: {self.chave_pix}')


class Banco:
    def __init__(self, numero_conta: int, agencia_banco: int, saldo_banco: float) -> None:
        self.numero_conta = numero_conta
        self.agencia_banco = agencia_banco
        self.saldo_banco = saldo_banco

    
    def set_clienteBanco(self, cliente: Cliente):
        self.cliente = cliente

    def get_clienteBanco(self):
        return self.cliente

    def set_pixBanco(self, pix: Pix):
        self.pix = pix

    def get_pixBanco(self):
        return self.pix

    def criarConta(self):
        contas_bancarias.append(self.numero_conta, self.agencia_banco, self.saldo_banco,self.cliente.nome_cliente, self.pix.chave_pix)

    def transferirValor(self, chave_pix_pagando: str, chave_pix_recebendo: str, valor_pix: float):
        self.chave_pix_pagando = chave_pix_pagando
        self.chave_pix_recebendo = chave_pix_recebendo
        self.valor_pix = valor_pix

        for busca in contas_bancarias:
            if chave_pix_pagando == chave_pix_recebendo:
                print(
                    '\n transferencia nao realizada\nObs: Voce nao pode transferir para você mesmo')
            else:
                if busca[contas_bancarias] == chave_pix_pagando:
                    saldoContaPaga = busca['saldo_banco']
                    if saldoContaPaga <= 0:
                        print('Saldo insuficiente')
                    else:
                        print(
                            f'Saldo antes da transferencia : {saldoContaPaga}')
                        saldoContaPaga -= self.chave_pix_banco.valor_pix
                        print(
                            f'Saldo depois da transferencia: {saldoContaPaga}')
                    if busca['chave_pix_banco'] == chave_pix_recebendo:
                        saldoContaRecebe = busca['saldo_banco']
                        print(
                            f'Saldo antes da transferencia: {saldoContaRecebe}')
                        saldoContaRecebe += self.chave_pix_banco.valor_pix
                        print(
                            f'Saldo depois da transferencia: {saldoContaRecebe}')


cliente1 = Cliente('Kayo', '12345')
contato1 = Contato('99999')
pix1 = Pix('kayo@gmail')
banco1 = Banco(333, 444, 1000)
banco1.set_clienteBanco(cliente1)
banco1.set_pixBanco(pix1)
banco1.criarConta(333, 444, 1000, 'kayo', 'kayo@gmail')

cliente2 = Cliente('Bia', '67890')
contato2 = Contato('88888')
pix2 = Pix('bia@gmail')
banco2 = Banco(111, 222, 500)
banco2.set_clienteBanco(cliente2)
banco2.set_pixBanco(pix2)
banco2.criarConta(111, 222, 500, 'bia', )

banco1.transferirValor('kayo@gmail', 'bia@gmail', 100)
