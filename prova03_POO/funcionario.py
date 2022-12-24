from bancoDados import connection
from funcao import Funcao


class Funcionario:
    def __init__(self, cpf, nome, funcao, salario, telefone):
        self.cpf = cpf
        self.nome = nome
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone

    def cadastrarFuncionario(self):
        with connection.cursor() as c:
            sql = f"INSERT INTO funcionario (cpf, nome, funcao, salario, telefone)" + \
                  f"VALUES ('{self.cpf}', '{self.nome}', '{self.funcao}', '{self.salario}', '{self.telefone}')"

            c.execute(sql)
            connection.commit()
            print('Cadastrado com sucesso')

    def pesquisarFuncionario(cpf_busca):
        with connection.cursor() as c:
            sql = f"SELECT * FROM funcionario"
            c.execute(sql)
            res_all = c.fetchall()
            print('Pesquisando...')

            for busca in res_all:
                if busca['cpf'] == cpf_busca:
                    print(f'Funcionario encontrado')
                    print(busca['nome'])
                    print(busca['cpf'])
                    return busca['cpf']

                print('CPF não encontrado')
                novo_cpf = input('Digite novamente o CPF: ')
                Funcionario.pesquisarFuncionario(novo_cpf)
                return busca['cpf']

    def editarFuncionario(cpf_busca):
        with connection.cursor() as c:
            cpf_pesquisa = Funcionario.pesquisarFuncionario(cpf_busca)

            opcesEditar = None
            while (opcesEditar != 0):
                print('--------------------------')
                print(
                    '\n1 - Novo nome\n2 - Nova Função\n3 - Novo Salario\n4 - Novo Telefone\n0 - Voltar ao Menu do Funcionario')
                print('--------------------------')

                opcesEditar = int(
                    input('Digite o numero da opcão que deseja fazer: '))

                if (opcesEditar == 1):
                    novo_nome = input('Novo Nome: ')
                    sql = f"UPDATE funcionario SET nome = '{novo_nome}' WHERE cpf = '{cpf_pesquisa}'"

                    c.execute(sql)
                    connection.commit()
                    print('Alterado com sucesso')

                if (opcesEditar == 2):
                    nova_funcao = input('Nova Função: ')
                    novo_id_funcao = Funcao.pesquisarFuncao_Cod(nova_funcao)
                    sql = f"UPDATE funcionario SET funcao = '{novo_id_funcao}' WHERE cpf = '{cpf_pesquisa}'"

                    c.execute(sql)
                    connection.commit()
                    print('Alterado com sucesso')

                if (opcesEditar == 3):
                    novo_salario = input('Novo Salario: ')

                    sql = f"UPDATE funcionario SET salario = '{novo_salario}' WHERE cpf = '{cpf_pesquisa}'"

                    c.execute(sql)
                    connection.commit()
                    print('Alterado com sucesso')

                if (opcesEditar == 4):
                    novo_telefone = input('Novo Telefone: ')

                    sql = f"UPDATE funcionario SET telefone = '{novo_telefone}' WHERE cpf = '{cpf_pesquisa}'"

                    c.execute(sql)
                    connection.commit()
                    print('Alterado com sucesso')

    def deletarFuncionario(cpf_busca):
        with connection.cursor() as c:
            cpf_pesquisa = Funcionario.pesquisarFuncionario(cpf_busca)

            sql = f"DELETE FROM funcionario WHERE cpf = '{cpf_pesquisa}'"

            c.execute(sql)
            connection.commit()
            print('Deletado com sucesso')
