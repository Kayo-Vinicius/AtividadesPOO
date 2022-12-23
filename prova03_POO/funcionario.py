import pymysql.cursors

opcoesMenu = None
menuFuncao = None
menuFuncionario = None

connection = pymysql.connect(host='localhost',  # Nome do host (servidor) do SGBD
                             user='root',  # Usuário que irá conectar ao banco
                             password='',  # Senha da conexão
                             database='prova03',  # Nome o banco que será utilizado
                             charset='utf8mb4',  # Conjunto de caracteres a utilizar
                             cursorclass=pymysql.cursors.DictCursor)  # Classe do cursor que será gerado


class Funcao:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    def cadastrarFuncao(self):
        with connection.cursor() as c:
          # Create a new record
            sql = f"INSERT INTO funcao (cod, nome)" + \
                  f"VALUES ('{self.codigo}', '{self.nome}')"

            c.execute(sql)
            connection.commit()  # Ultizado para quando vou alterar alguma coisa na tebela
            print('Cadastrado com sucesso')

    def pesquisarFuncao(codigo):
        with connection.cursor() as c:
            sql = f"SELECT * FROM funcao"
            c.execute(sql)
            res_all = c.fetchall()
            print('Pesquisando...')

            for busca in res_all:
                if busca['cod'] == codigo:
                    print(f'Função encontrada')
                    print(busca['nome'])
                    return busca['cod']

            print('Função não encontrada')
            codigo = input('Digite novamente: ')
            Funcao.pesquisarFuncao(codigo)

    def buscar_Id_Funcao(nome_funcao):
        with connection.cursor() as c:
            sql = f"SELECT * FROM funcao"
            c.execute(sql)
            res_all = c.fetchall()
            print('Pesquisando...')

            for busca in res_all:
                if busca['nome'] == nome_funcao:
                    print(f'Função encontrada')
                    print(busca['id'])
                    return busca['id']

            print('ID da função não encontrado')
            nome_funcao = input('Digite novamente: ')
            Funcao.buscar_Id_Funcao(nome_funcao)

    def editarFuncao(codigo_busca):
        with connection.cursor() as c:
            codigo_pesquisa = Funcao.buscarFuncao(codigo_busca)
            novo_codigo = input('Novo codigo: ')
            sql = f"UPDATE funcao SET cod = '{novo_codigo}' WHERE cod = '{codigo_pesquisa}'"

            c.execute(sql)
            connection.commit()
            print('Alterado com sucesso')

    def deletarFuncao(codigo_busca):
        with connection.cursor() as c:
            codigo_pesquisa = Funcao.buscarFuncao(codigo_busca)
            sql = f"DELETE FROM funcao WHERE cod = '{codigo_pesquisa}'"

            c.execute(sql)
            connection.commit()
            print('Deletado com sucesso')


class Funcionario():
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
                    print(f'Função encontrada')
                    print(busca['nome'])
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

                opcesEditar = int(input('Digite o numero da opcão que deseja fazer: '))

                if (opcesEditar == 1):
                    novo_nome = input('Novo Nome: ')
                    sql = f"UPDATE funcionario SET nome = '{novo_nome}' WHERE cpf = '{cpf_pesquisa}'"

                    c.execute(sql)
                    connection.commit()
                    print('Alterado com sucesso')

                if (opcesEditar == 2):
                    nova_funcao = input('Nova Função: ')
                    novo_id_funcao = Funcao.buscar_Id_Funcao(nova_funcao)
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


while (opcoesMenu != 0):
    print('--------------------------')
    print('\n1 - Manter Funções\n2 - Manter Funcionários\n0 - Sair')
    print('--------------------------')
    opcoesMenu = int(input('Digite o numero da opcão que deseja fazer: '))

    if (opcoesMenu == 1):
        while (menuFuncao != 0):
            print('--------------------------')
            print('\n1 - Cadastrar Funcao\n2 - Pesquisar Funcao\n3 - Editar Funcao\n4 - Deletar Funcao\n0 - Voltar ao Menu Principal')
            print('--------------------------')
            menuFuncao = int(
                input('Digite o numero da opcão que deseja fazer: '))

            if (menuFuncao == 1):
                codigo = input('Codigo: ')
                nome = input('Nome: ')

                funcao = Funcao(codigo, nome)
                funcao.cadastrarFuncao()

            if (menuFuncao == 2):
                codigo = input(
                    'Digite o codigo da função que deseja PESQUISAR: ')

                Funcao.pesquisarFuncao(codigo)

            if (menuFuncao == 3):
                codigo = input(
                    'Digite o codigo da função que deseja ALTERAR: ')

                Funcao.editarFuncao(codigo)

            if (menuFuncao == 4):
                codigo = input(
                    'Digite o codigo da função que deseja DELETAR: ')

                Funcao.deletarFuncao(codigo)

    if (opcoesMenu == 2):
        while (menuFuncionario != 0):
            print('--------------------------')
            print('\n1 - Cadastrar Funcionario\n2 - Pesquisar Funcionario\n3 - Editar Funcionario\n4 - Deletar Funcionario\n0 - Voltar ao Menu Principal')
            print('--------------------------')
            menuFuncionario = int(
                input('Digite o numero da opcão que deseja fazer: '))

            if (menuFuncionario == 1):
                cpf = input('CPF: ')
                nome = input('Nome: ')
                funcao = input('Função: ')
                salario = float(input('Salario: '))
                telefone = input('Telefone: ')

                id_funcao = Funcao.buscar_Id_Funcao(funcao)

                funcionario = Funcionario(
                    cpf, nome, id_funcao, salario, telefone)
                Funcionario.cadastrarFuncionario(funcionario)

            if (menuFuncionario == 2):
                cpf = input('Digite o CPF do funcionario que deseja PESQUISAR: ')

                Funcionario.pesquisarFuncionario(cpf)

            if (menuFuncionario == 3):
                cpf = input('Digite o CPF do funcionario que deseja EDITAR: ')

                Funcionario.editarFuncionario(cpf)

            if (menuFuncionario == 4):
                cpf = input('Digite o CPF do funcionario que deseja DELETAR: ')

                Funcionario.deletarFuncionario(cpf)
