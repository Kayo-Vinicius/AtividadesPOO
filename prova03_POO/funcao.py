from bancoDados import connection


class Funcao:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    def cadastrarFuncao(self):
        with connection.cursor() as c:
            sql = f"INSERT INTO funcao (cod, nome)" + \
                  f"VALUES ('{self.codigo}', '{self.nome}')"

            c.execute(sql)
            connection.commit()
            print('Cadastrado com sucesso')

    def pesquisarFuncao_Cod(codigo_busca):
        with connection.cursor() as c:
            sql = f"SELECT * FROM funcao"
            c.execute(sql)
            res_all = c.fetchall()
            print('Pesquisando...')

            for busca in res_all:
                if busca['cod'] == codigo_busca:
                    print(f'Função encontrada')
                    print(busca['nome'])
                    return busca['id']

            print('Função não encontrada')
            codigo_busca = input('Digite o novamente CODIGO: ')
            Funcao.pesquisarFuncao_Cod(codigo_busca)

    def pesquisarFuncao_Nome(nome_busca):
        with connection.cursor() as c:
            sql = f"SELECT * FROM funcao"
            c.execute(sql)
            res_all = c.fetchall()
            print('Pesquisando...')

            for busca in res_all:
                if busca['nome'] == nome_busca:
                    print(f'ID encontrado')
                    print(busca['id'])
                    return busca['id']

            print('Função não encontrado')
            nome_busca = input('Digite novamente o NOME: ')
            Funcao.pesquisarFuncao_Nome(nome_busca)

    def editarFuncao(codigo_busca):
        with connection.cursor() as c:
            codigo_pesquisa = Funcao.pesquisarFuncao_Cod(codigo_busca)
            novo_codigo = input('Novo codigo: ')
            sql = f"UPDATE funcao SET cod = '{novo_codigo}' WHERE id = '{codigo_pesquisa}'"

            c.execute(sql)
            connection.commit()
            print('Alterado com sucesso')

    def deletarFuncao(codigo_busca):
        with connection.cursor() as c:
            codigo_pesquisa = Funcao.pesquisarFuncao_Cod(codigo_busca)

            sql = f"DELETE FROM funcao WHERE id = '{codigo_pesquisa}'"

            c.execute(sql)
            connection.commit()
            print('Deletado com sucesso')
