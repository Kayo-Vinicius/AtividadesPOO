opcoesMenu = None
professores = []
alunos = []
tecnicos = []

class Professor:
    def __init__(self, nome, formacao, salario) -> None:
        self.nome = nome
        self.formacao = formacao
        self.salario = salario

    def addProfessor(self, nome, formacao, salario):
        professores.append(Professor(nome, formacao, salario))
    
    def imprimirProfessor(self):
        print('\n-------------------Dados do Professor---------------')
        print(f'Nome: {self.nome} \nFormacao: {self.formacao} \nSalario: {self.salario}')

class Aluno():
    def __init__(self, nome, curso, matricula, anoEntrada) -> None:
        self.nome = nome
        self.curso = curso
        self.matricula = matricula
        self.anoEntrada = anoEntrada

    def addAluno(self, nome, curso, matricula, anoEntrada):
        alunos.append(Aluno(nome, curso, matricula, anoEntrada))

    def imprimirAluno(self):
        print('\n-------------------Dados do Aluno-------------------')
        print(f'Nome: {self.nome} \nCurso: {self.curso} \nMatricula: {self.matricula} \nAno de Entrada: {self.anoEntrada}')

class Tecnico():
    def __init__(self, nome, areaAtuacao) -> None:
        self.nome = nome
        self.areaAtuacao = areaAtuacao

    def addTecnico(self, nome, areaAtuacao):
        tecnicos.append(Tecnico( nome, areaAtuacao))

    def imprimirTecnico(self):
        print('\n-------------------Dados do Tecnico-----------------')
        print(f'Nome: {self.nome} \nArea de Atuacao: {self.areaAtuacao}')

p1 = Professor('Francois', 'Programacao', '1000')
p1.imprimirProfessor()

t1 = Tecnico('Luis', 'Professor')
t1.imprimirTecnico()

a1 = Aluno('Kayo', 'Computacao', '1111', '2021')
a1.imprimirAluno()




'''
while(opcoesMenu != 0):
    print('--------------------------')
    print('1 - Adicionar Professor\n2 - Adicionar Aluno\n3 - Adicionar Tecnico\n4 - Mostrar Dados\n0 - Sair')
    print('--------------------------')
    opcoesMenu = int(input('Digite o numero da opcão que deseja fazer: '))
    
    if opcoesMenu == 1:
        nomeProfessor = input('Nome do Professor: ')
        formacao = input('Formação do Professor: ')
        salario = int(input('Salario: '))

        Professor.addProfessor(nomeProfessor, formacao, salario)
        Professor.imprimirContas()

    elif opcoesMenu == 2:
        nomeAluno = input('Nome Aluno: ')
        curso = input('Curso: ')
        matricula = input('Matricula: ')
        anoEntrada = int(input('Ano de entrada: '))

        Aluno.addAluno(nomeAluno, curso, matricula, anoEntrada)
'''