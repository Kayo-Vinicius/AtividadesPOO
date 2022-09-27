funcionarios = []
telefones = []
opcoesMenu = None
opcoesEditar = None

def cadastrarFuncionario(nomeFuncionario, cpfFuncionario, cargoFuncionario, salarioFuncionario, telefoneFuncionario):
   novoFuncionario = {'nome': nomeFuncionario, 'cpf': cpfFuncionario, 
   'cargo': cargoFuncionario, 'salario' : salarioFuncionario, 'telefone' : telefoneFuncionario}
   print('Funcionario cadastrado com sucesso com sucesso')
   return novoFuncionario

def buscarFuncionario(cpfFuncionario):
   for busca in funcionarios:
      if busca['cpf'] == cpfFuncionario:
         print('Funcionario encontrado')
         return busca
      else:
         print('Funcionario não encontrado digite novamente')
         cpfFuncionario = input('CPF: ')
         return buscarFuncionario(cpfFuncionario)

def excluirFuncionario(cpfFuncionario):
   for busca in funcionarios:
      if busca['cpf'] == cpfFuncionario:
         print('Funcionario encontrado')
         funcionarios.remove(busca)
         print('Funcionario removido')
      elif busca['cpf'] != cpfFuncionario:
         print('CPF não encontrado digite novamente')
         cpfFuncionario = input('CPF: ')
         return excluirFuncionario(cpfFuncionario)

def novoTelefone(cpfFuncionario):
   for busca in funcionarios:
      if busca['cpf'] == cpfFuncionario:
         novoNumero = input('Digite o novo numero: ')
         telefones.append(novoNumero)
         busca['telefone'] = telefones
      elif busca['cpf'] != cpfFuncionario:
         print('CPF não encontrado digite novamente')
         cpfFuncionario = input('CPF: ')
         return novoTelefone(cpfFuncionario)
            
def editarFuncionario(cpfFuncionario):
   for busca in funcionarios:
      if busca['cpf'] == cpfFuncionario:
         print('Conta encontrada') 

         print('\n1 - Novo nome\n2 - Novo cpf\n3 - Novo cargo\n4 - Novo salario\n5 - Novo telefone\n0 - Sair')
         opcoesEditar = int(input('Digite o numero da opcão que deseja fazer: '))

         if opcoesEditar == 1:
            print('Nome antigo: ', busca['nome'])
            novoNome = input('Novo nome: ')
            busca['nome'] = novoNome
            print('Nome atual: ', busca['nome'])
            return busca

         elif opcoesEditar == 2:
            print('CPF antigo: ', busca['cpf'])
            novoCPF = input('Novo CPF: ')
            busca['cpf'] = novoCPF
            print('CPF atual: ', busca['cpf'])
            return busca
                
         elif opcoesEditar == 3:
            print('Cargo antigo: ', busca['cargo'])
            novoCargo = input('Novo cargo: ')
            busca['cargo'] = novoCargo
            print('Cargo atual: ', busca['cargo'])
            return busca
                
         elif opcoesEditar == 4:
            print('Salario antigo: ', busca['salario'])
            novoSalario = float(input('Novo salario: '))
            busca['salario'] = novoSalario
            print('Salario atual: ', busca['salario']) 
            return busca 

         elif opcoesEditar == 5:
            print('Telefone antigo: ', busca['telefone'])
            novoTelefone = input('Novo telefone: ')
            busca['telefone'] = novoTelefone
            print('Telefone atual: ', busca['telefone'])
            return busca

      elif busca['cpf'] != cpfFuncionario:
         print('CPF não encontrado digite novamente')
         cpfFuncionario = input('CPF: ')
         return editarFuncionario(cpfFuncionario)    
            

while(opcoesMenu != 0):
   if not funcionarios:
      print('Não tem nenhum funcionario cadastrado\nCadastre um primeiro')
      nome = input('Nome: ')
      cpf = input('CPF: ')
      cargo = input('Cargo: ')
      salario = float(input('Salario: '))
      numeroTel = input('Telefone: ')
      
      telefones.append(numeroTel)
      funcionarios.append(cadastrarFuncionario(nome, cpf, cargo, salario, telefones))
      print(funcionarios)

   else:
      print('\n1 - Cadastrar Funcionario\n2 - Buscar Funcionario\n0 - Sair')
      opcoesMenu = int(input('Digite o numero da opcão que deseja fazer: '))

      if opcoesMenu == 1:
         nome = input('Nome: ')
         cpf = input('CPF: ')
         cargo = input('Cargo: ')
         salario = float(input('Salario: '))
         numeroTel = input('Telefone: ')
      
         telefones.append(numeroTel)
         funcionarios.append(cadastrarFuncionario(nome, cpf, cargo, salario, telefones))
         print(funcionarios)
      
      elif opcoesMenu == 2:
         cpf = input('Digite o CPF do funcionario: ')
         buscarFuncionario(cpf)
         print('\n3 - Novo telefone\n4 - Editar dados do funcionario\n5 - Excluir Funcionario\n0 - Sair')
         opcoesMenu = int(input('Digite o numero da opcão que deseja fazer: '))

         if opcoesMenu == 3:
            cpf = input('Digite o CPF do funcionario: ')
            novoTelefone(cpf)
            print(funcionarios)

         elif opcoesMenu == 4:
            cpf = input('Digite o CPF do funcionario: ')
            editarFuncionario(cpf)
            print(funcionarios)

         elif opcoesMenu == 5:
            cpf = input('Digite o CPF do funcionario: ')
            excluirFuncionario(cpf)   