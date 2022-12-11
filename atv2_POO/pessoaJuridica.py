class Fornecedor():
    def __init__(self, nomeFornecedor) -> None:                                                                         
        self.nomeFornecedor = nomeFornecedor
        self.fornecedores = []

    def addFornecedor(self, nomeFornecedor):
        self.fornecedores.append(Fornecedor(nomeFornecedor))
    
    def imprimirFornecedor(self):
        for busca in self.fornecedores:
            print(f'Dados: {busca.nomeFornecedor}')

class EmpresaJr():
    def __init__(self, nomeEmpresajr) -> None:
        self.nomeEmpresajr = nomeEmpresajr
        self.empresas = []

    def addEmpresajr(self, nomeEmpresajr):
        self.empresas.append(EmpresaJr(nomeEmpresajr))
    
    def imprimirEmpresajr(self):
        for busca in self.empresas:
            print(f'Dados: {busca.nomeEmpresajr}')