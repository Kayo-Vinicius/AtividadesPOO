#1 Questao

agenda = []
opcoesMenu = None

def criarAgenda(cpfPessoa, nomePessoa, idadePessoa, telefonePessoa):
	novaPessoa = [{'cpf':cpfPessoa}, nomePessoa, idadePessoa, telefonePessoa]
	return novaPessoa
	
print('Informe seus dados')
cpfPessoa = input('CPF: ')
nomePessoa = input('Nome: ')    
idadePessoa = int(input('Idade: '))
telefonePessoa = input('Telefone: ')

agenda.append(criarAgenda(cpfPessoa, nomePessoa, idadePessoa, telefonePessoa))

print(agenda)