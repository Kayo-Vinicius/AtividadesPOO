#import pessoaFisica
opcoesMenu = None
curso = []

class Curso():
    def __init__(self, nomeCurso, descricao, disciplinas, cargaHoraria) -> None:
        self.nomeCurso = nomeCurso
        self.descricao = descricao
        self.disciplinas = disciplinas
        self.cargaHoraria = cargaHoraria

    def addCurso(self, nomeCurso, descricao, disciplinas, cargaHoraria):
        curso.append(Curso(nomeCurso, descricao, disciplinas, cargaHoraria))
        print(curso)
    
    def imprimirContas(self):
        print(f'Dados: {self.nomeCurso, self.descricao, self.disciplinas, self.cargaHoraria}')


while(opcoesMenu != 0):
    print('--------------------------')
    print('1 - Manter Aluno\n2 - Manter Curso\n3 - Manter Disciplina\n4 - Matricular Aluno\n5 - Listar Alunos\n0 - Sair')
    print('--------------------------')
    opcoesMenu = int(input('Digite o numero da opcão que deseja fazer: '))
    
    if opcoesMenu == 1:
        nomeCurso = input('Nome do Curso: ')
        descricao = input('Descricao do curso: ')
        disciplinas = input('Disciplinas: ')
        cargaHoraria = input('Carga Horaria: ')

        Curso.addCurso(nomeCurso, descricao, disciplinas, cargaHoraria)

        