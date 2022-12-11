opcoesMenu = None

class Professor():
    def __init__(self, nome: str, formacao: str, salario: float) -> None:
        self.nome = nome
        self.formacao = formacao
        self.salario = salario
        self.professores = []

    def addProfessor(self, nome, formacao, salario):
        self.professores.append(Professor(nome, formacao, salario))
    
    def imprimirProfessor(self):
        for busca in self.professores:
            print('\n-------------------Dados do Professor---------------')
            print(f'Nome: { busca.nome} \nFormacao: {busca.formacao} \nSalario: {busca.salario}')

class Aluno():
    def __init__(self, nomeAluno: str, curso: str, matricula: int, anoEntrada: int) -> None:
        self.nomeAluno = nomeAluno
        self.curso = curso
        self.matricula = matricula
        self.anoEntrada = anoEntrada
        self.alunos = []
        self.alunosMatriculados = []

    def addAluno(self, nomeAluno, curso, matricula, anoEntrada):
        self.alunos.append(Aluno(nomeAluno, curso, matricula, anoEntrada))
        self.alunosMatriculados = {'nomeAluno': nomeAluno}

    def imprimirAluno(self):
        for busca in self.alunos:
            print('\n-------------------Dados do Aluno-------------------')
            print(f'Nome: {busca.nomeAluno} \nCurso: {busca.curso} \nMatricula: {busca.matricula} \nAno de Entrada: {busca.anoEntrada}')

    def pesquisarAluno(self, nome):
        print('nao deu certo')
        for busca in self.alunosMatriculados:
            print('deu certo')
            if busca['nomeAluno'] == nome:
                print('Aluno já existe')
            else:
                print('Não e')
    
class Tecnico():
    def __init__(self, nome, areaAtuacao) -> None:
        self.nome = nome
        self.areaAtuacao = areaAtuacao
        self.tecnicos = []

    def addTecnico(self, nome, areaAtuacao):
        self.tecnicos.append(Tecnico( nome, areaAtuacao))

    def imprimirTecnico(self):
        for busca in self.tecnicos:
            print('\n-------------------Dados do Tecnico-----------------')
            print(f'Nome: {busca.nome} \nArea de Atuacao: {busca.areaAtuacao}')
'''
p1 = Professor('Francois', 'Programacao', '1000')
p1.imprimirProfessor()

t1 = Tecnico('Luis', 'Professor')
t1.imprimirTecnico()

a1 = Aluno('Kayo', 'Computacao', '1111', '2021')
a1.imprimirAluno()





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