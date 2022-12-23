from funcao import Funcao
from funcionario import Funcionario

opcoesMenu = None
menuFuncao = None
menuFuncionario = None

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
            menuFuncao = int(input('Digite o numero da opcão que deseja fazer: '))

            if (menuFuncao == 1):
                codigo = input('Codigo da Função: ')
                nome = input('Nome da Função: ')

                funcao = Funcao(codigo, nome)
                Funcao.cadastrarFuncao(funcao)

            if (menuFuncao == 2):
                codigo = input('Digite o CODIGO da função que deseja PESQUISAR: ')

                Funcao.pesquisarFuncao_Cod(codigo)

            if (menuFuncao == 3):
                codigo = input('Digite o CODIGO da função que deseja ALTERAR: ')

                Funcao.editarFuncao(codigo)

            if (menuFuncao == 4):
                codigo = input('Digite o CODIGO da função que deseja DELETAR: ')

                Funcao.deletarFuncao(codigo)

    if (opcoesMenu == 2):
        while (menuFuncionario != 0):
            print('--------------------------')
            print('\n1 - Cadastrar Funcionario\n2 - Pesquisar Funcionario\n3 - Editar Funcionario\n4 - Deletar Funcionario\n0 - Voltar ao Menu Principal')
            print('--------------------------')
            menuFuncionario = int(input('Digite o numero da opcão que deseja fazer: '))

            if (menuFuncionario == 1):
                cpf = input('CPF: ')
                nome = input('Nome: ')
                funcao = input('Codigo da Função: ')
                salario = float(input('Salario: '))
                telefone = input('Telefone: ')

                id_funcao = Funcao.pesquisarFuncao_Cod(funcao)

                funcionario = Funcionario(cpf, nome, id_funcao, salario, telefone)
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
