#3 Questao

dicionarioPrincipal = []
dicionarioBackup = []
opcoesMenu = None

def cadastrarPessoa(cpfPessoa, nomePessoa, idadePessoa, telefonePessoa, sexoPessoa):
	novaPessoa = {'cpf': cpfPessoa, 'nome':nomePessoa, 'idade':idadePessoa, 'telefone':telefonePessoa, 'sexo':sexoPessoa}
	return novaPessoa

while(opcoesMenu != 0):
  print('0-Sair\n1-Adicionar Pessoa\n')
  opcoesMenu = int(input('Digite a opçao que deseja: '))

  if opcoesMenu == 1:
    print('Informe seus dados')
    cpfPessoa = input('CPF: ')
    nomePessoa = input('Nome: ')
    idadePessoa = int(input('Idade: '))
    telefonePessoa = input('Telefone: ')
    sexoPessoa = input('Sexo: ')

    dicionarioPrincipal.append(cadastrarPessoa(cpfPessoa, nomePessoa, idadePessoa, telefonePessoa, sexoPessoa))

    if len(dicionarioPrincipal) == 5:
      dicionarioBackup.append(dicionarioPrincipal.copy())
      dicionarioPrincipal.clear()

    print('Principal: ', dicionarioPrincipal)
    print('Backup: ', dicionarioBackup)
