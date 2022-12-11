from pessoaFisica import Professor
from pessoaFisica import Aluno
from pessoaFisica import Tecnico
from curso import Curso
from pessoaJuridica import EmpresaJr
from pessoaJuridica import Fornecedor

opcoesMenu = None

while (opcoesMenu != 0):
    print('--------------------------')
    print('1 - Adicionar Curso\n2 - Adicionar Professor\n3 - Adicionar Tecnico\n4 - Adicionar Aluno \n5 - Adicionar Fornecedor\n6 - Adicionar EmpresaJr\n7 - pesquisar Aluno\n0 - Sair')
    print('--------------------------')
    opcoesMenu = int(input('Digite o numero da opcão que deseja fazer: '))
    
    if opcoesMenu == 1:
        nomeCurso = input('Nome do Curso: ')
        descricao = input('Descricao do curso: ')
        disciplinas = input('Disciplinas: ')
        cargaHoraria = input('Carga Horaria: ')

        curso = Curso(nomeCurso, descricao, disciplinas, cargaHoraria)
        curso.addCurso(nomeCurso, descricao, disciplinas, cargaHoraria)
        curso.imprimirCurso()

    if opcoesMenu == 2:
        nomeProfessor = input('Nome do Professor: ')
        formacao = input('Formação do Professor: ')
        salario = int(input('Salario: '))

        professor = Professor(nomeProfessor, formacao, salario)
        professor.addProfessor(nomeProfessor, formacao, salario)
        professor.imprimirProfessor()

    if opcoesMenu == 3:
        nomeTecnico = input('Nome do Tecnico: ')
        areaAtuacao = input('Area de atuação: ')

        tecnico = Tecnico(nomeTecnico, areaAtuacao)
        tecnico.addTecnico(nomeTecnico, areaAtuacao)
        tecnico.imprimirTecnico()

    if opcoesMenu == 4:
        nomeAluno = input('Nome do Aluno: ')
        curso = input('Curso: ')
        matricula = input('Matricula: ')
        anoEntrada = int(input('Ano de entrada: '))

        aluno = Aluno(nomeAluno, curso, matricula, anoEntrada)
        aluno.addAluno(nomeAluno, curso, matricula, anoEntrada)
        aluno.imprimirAluno()

        print(aluno.alunos)

    if opcoesMenu == 5:
        nomeFornecedor = input('Nome do Fornecedor: ')

        fornecedor = Fornecedor(nomeFornecedor)
        fornecedor.addFornecedor(nomeFornecedor)
        fornecedor.imprimirFornecedor()

    if opcoesMenu == 6:
        nomeEmpresajr = input('Nome da Empresa: ')

        empresa = EmpresaJr(nomeEmpresajr)
        empresa.addEmpresajr(nomeEmpresajr)
        empresa.imprimirEmpresajr()

    if opcoesMenu == 7:
        nomeAluno = input('Nome do Aluno: ')
        curso = input('Curso: ')
        matricula = int(input('Matricula: '))
        anoEntrada = int(input('Ano de entrada: '))

        buscarAluno = Aluno(nomeAluno, curso, matricula, anoEntrada)
        buscarAluno.pesquisarAluno(nomeAluno)

        