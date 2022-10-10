# 2 Questao
agenda = []
agendaMenorIdade = []
opcoesMenu = None


def criarDicionario(cpfPessoa, nomePessoa, idadePessoa):
    novaPessoa = {'cpf': cpfPessoa, 'nome': nomePessoa, 'idade': idadePessoa}
    return novaPessoa


def removerMenorIdade():
    for busca in agenda:
        if busca['idade'] < 18:
            print('Pessoa com menos de 18 anos')
            agendaMenorIdade.append(busca)
            print('Pessoa transferida para a agenda de menores de 18 anos')
            agenda.remove(busca)


while (opcoesMenu != 0):
    print('0-Sair\n1-Adicionar Pessoa\n')
    opcoesMenu = int(input('Digite a opçao que deseja: '))

    if opcoesMenu == 1:
        print('Informe seus dados')
        cpfPessoa = input('CPF: ')
        nomePessoa = input('Nome: ')
        idadePessoa = int(input('Idade: '))
        telefonePessoa = input('Telefone: ')

        agenda.append(criarDicionario(cpfPessoa, nomePessoa, idadePessoa))
        print(agenda)
        print(agendaMenorIdade)
        removerMenorIdade()
        print(agendaMenorIdade)
        print(agenda)
