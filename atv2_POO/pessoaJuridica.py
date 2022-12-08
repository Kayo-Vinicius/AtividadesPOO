pessoas_juridicas = []

class Fornecedor():
    def __init__(self, nome_fornecedor) -> None:                                                                         
        self.nome_fornecedor = nome_fornecedor

    def addFornecedor(self, nome_fornecedor):
        pessoas_juridicas.append(Fornecedor(nome_fornecedor))
    
    def imprimirFornecedor(self):
        print(f'Dados: {self.nome_fornecedor}')

class EmpresaJr():
    def __init__(self, nome_empresajr) -> None:
        self.nome_empresajr = nome_empresajr

    def addProfessor(self, nome_empresajr):
        pessoas_juridicas.append(EmpresaJr(nome_empresajr))
    
    def imprimirEmpresa(self):
        print(f'Dados: {self.nome_empresajr}')