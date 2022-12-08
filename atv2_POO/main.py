from pessoaFisica import Professor
from pessoaFisica import Aluno
from pessoaFisica import Tecnico
from curso import Curso

opcoesMenu = None

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

    elif opcoesMenu == 2:
        nomeProfessor = input('Nome do Professor: ')
        formacao = input('Formação do Professor: ')
        salario = int(input('Salario: '))

        Professor.addProfessor(nomeProfessor, formacao, salario)
        Professor.imprimir()

    elif opcoesMenu == 3:
        print('ijwwe')

    elif opcoesMenu == 4:
        nomeAluno = input('Nome Aluno: ')
        curso = input('Curso: ')
        matricula = input('Matricula: ')
        anoEntrada = int(input('Ano de entrada: '))

        Aluno.addAluno(nomeAluno, curso, matricula, anoEntrada)

    elif opcoesMenu == 5:
        Aluno.imprimirAluno()