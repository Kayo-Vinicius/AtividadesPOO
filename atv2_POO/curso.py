from pessoaFisica import Aluno
opcoesMenuCurso = None

class Curso():
    def __init__(self, nomeCurso: str, descricao: str, disciplinas: str, cargaHoraria: int) -> None:
        self.nomeCurso = nomeCurso
        self.descricao = descricao
        self.disciplinas = disciplinas
        self.cargaHoraria = cargaHoraria
        self.cursos = []

    def addCurso(self, nomeCurso, descricao, disciplinas, cargaHoraria):
        self.cursos.append(Curso(nomeCurso, descricao, disciplinas, cargaHoraria))

    def imprimirCurso(self):
        for busca in self.cursos:
            print('\n-------------------Dados do Curso-------------------')
            print(f'Nome do Curso: {busca.nomeCurso}\nDescrição: {busca.descricao}\nDisciplinas: {busca.disciplinas}\nCarga Horaria:  {busca.cargaHoraria}')

while(opcoesMenuCurso != 0):
    print('--------------------------')
    print('1 - Manter Aluno\n2 - Manter Curso\n3 - Manter Disciplina\n4 - Matricular Aluno\n5 - Listar Alunos\n0 - Sair')
    print('--------------------------')
    opcoesMenu = int(input('Digite o numero da opcão que deseja fazer: '))

    if opcoesMenuCurso == 1:
        nomeAluno = input('Nome do Aluno: ')
        curso = input('Curso: ')
        matricula = input('Matricula: ')
        anoEntrada = int(input('Ano de entrada: '))

        buscarAluno = Curso(nomeAluno, curso, matricula, anoEntrada)
        buscarAluno.pesquisarAluno(nomeAluno, curso, matricula, anoEntrada)
    
    if opcoesMenu == 2:
        nomeCurso = input('Nome do Curso: ')
        descricao = input('Descricao do curso: ')
        disciplinas = input('Disciplinas: ')
        cargaHoraria = input('Carga Horaria: ')

        curso = Curso(nomeCurso, descricao, disciplinas, cargaHoraria)
        curso.addCurso(nomeCurso, descricao, disciplinas, cargaHoraria)
        curso.imprimirCurso()

    if opcoesMenu == 4:
        nomeAluno = input('Nome Aluno: ')
        curso = input('Curso: ')
        matricula = input('Matricula: ')
        anoEntrada = int(input('Ano de entrada: '))

        aluno = Aluno(nomeAluno, curso, matricula, anoEntrada)
        aluno.addAluno(nomeAluno, curso, matricula, anoEntrada)
        aluno.imprimirAluno()

    if opcoesMenu == 5:
        Aluno.imprimirDados()
    
    if opcoesMenu == 7:
        nomeAluno = input('Nome do Aluno: ')
        curso = input('Curso: ')
        matricula = int(input('Matricula: '))
        anoEntrada = int(input('Ano de entrada: '))

        buscarAluno = Curso(nomeAluno, curso, matricula, anoEntrada)
        buscarAluno.pesquisarAluno(nomeAluno, curso, matricula, anoEntrada)
