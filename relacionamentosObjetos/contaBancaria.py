class Cliente:
    def __init__(self, nome_cliente: str, cpf_cliente: int) -> None:
        self.nome_cliente = nome_cliente
        self.cpf_cliente = cpf_cliente  

class Banco:
    def __init__(self, nome_banco: str, agencia_banco: int) -> None:
        self.nome_banco = nome_banco
        self.agencia_banco = agencia_banco
    
class Contato:
    def __init__(self, telefone_contato: str) -> None:
        self.telefone_contato = telefone_contato
        
    def set_clienteBanco(self, cliente: Cliente):
        self.cliente = cliente

    def get_clienteBanco(self):
        return self.cliente

    def dadosContato(self):
        print(f'Nome: {self.cliente.nome_cliente} Contato: {self.telefone_contato}')

class Pix:
    def set_clienteBanco(self, cliente: Cliente):
        self.cliente = cliente

    def get_clienteBanco(self):
        return self.cliente

    def set_banco(self, banco: Banco):
        self.banco = banco
    
    def get_banco(self):
        return self.banco

    def dadosCliente(self):
        print(f'Nome: {self.cliente.nome_cliente} CPF: {self.cliente.cpf_cliente} Banco: {self.banco.nome_banco} Agencia: {self.banco.agencia_banco}')

obj_cliente = Cliente('Kayo', '12345')
obj_banco = Banco('Brasil', '11111')
obj_contato = Contato('99999')
obj_pix = Pix()

obj_pix.set_clienteBanco(obj_cliente)
obj_pix.set_banco(obj_banco)
obj_contato.set_clienteBanco(obj_cliente)
obj_contato.dadosContato()
obj_pix.dadosCliente()

obj_cliente = Cliente('Bia', '67890')
obj_banco = Banco('Bradesco', '22222')
obj_contato = Contato('77777')
obj_pix = Pix()

obj_pix.set_clienteBanco(obj_cliente)
obj_pix.set_banco(obj_banco)
obj_contato.set_clienteBanco(obj_cliente)
obj_contato.dadosContato()
obj_pix.dadosCliente()