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
        elif busca['cpf'] != cpfFuncionario:
            print('Funcionario não digite novamente')
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
          #telefones.apend(novoNumero)
         busca['telefone'] = telefones.apend(novoNumero)
      elif busca['cpf'] != cpfFuncionario:
         print('CPF não encontrado digite novamente')
         cpfFuncionario = input('CPF: ')
         return novoTelefone(cpfFuncionario)
            
def editarFuncionario(cpfFuncionario):
   for busca in funcionarios:
      if busca['cpf'] == cpfFuncionario:
         print('Conta encontrada')
            
         while(opcoesEditar != 0):  
            print('\n1 - Novo nome\n2 - Novo cpf\n3 - Novo cargo\n4 - Novo salario\n5 - Novo telefone\n0 - Sair')
            opcoesEditar = int(input('Digite o numero da opcão que deseja fazer: '))

            if opcoesEditar == 1:
               print('Nome antigo: ', busca['nome'])
               novoNome = input('Novo nome: ')
               busca['nome'] = novoNome
               print('Nome atual: ', busca['nome'])

            elif opcoesEditar == 2:
               novoCPF = input('Novo CPF: ')
               busca['cpf'] = novoCPF
                
            elif opcoesEditar == 3:
               novoCargo = input('Novo cargo: ')
               busca['cargo'] = novoCargo
                
            elif opcoesEditar == 4:
               novoSalario = float(input('Novo salario: '))
               busca['salario'] = novoSalario 
                    
            elif opcoesEditar == 5:
               novoTelefone = input('Novo telefone: ')
               busca['telefone'] = novoTelefone

      elif busca['cpf'] != cpfFuncionario:
         print('CPF não encontrado digite novamente')
         cpfFuncionario = input('CPF: ')
         return editarFuncionario(cpfFuncionario)    
            

while(opcoesMenu != 0):
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
    
   elif opcoesMenu == 2 and funcionarios == None:
      print('Cadastre um funcionario primeiro')
   elif opcoesMenu == 2 and funcionarios != None:
      print('\n3 - Novo telefone\n4 - Editar dados do funcionario\n5 - Excluir Funcionario')
      opcoesMenu = int(input('Digite o numero da opcão que deseja fazer: '))

      if opcoesMenu == 3:
         cpf = input('CPF: ')
         novoTelefone(cpf)

      elif opcoesMenu == 4:
         cpf = input('CPF: ')
         editarFuncionario(cpf)

      elif opcoesMenu == 5:
         cpf = input('CPF: ')
         excluirFuncionario(cpf)
      
     