# Lista de alunos
alunos = []

# RA dos alunos
ra = 0

# Função Menu
def menu():
    while True:
        print(f'\n=== MENU ===\n1. Cadastrar Aluno\n2. Listar Alunos\n3. Média da turma\n4. Buscar aluno\n5. Sair\n')
        escolha = input('Escolha: ')

        if escolha == "1":
            print('\n')
            cadastrarAluno()
        elif escolha == "2":
            print('\n')
            listarAlunos()
        elif escolha == "3":
            print('\n')
            mediaTurma()
        elif escolha == "4":
            print('\n')
            buscarAluno()
        elif escolha == "5":
            print("saindo...")
            break
        else:
            print('Escolha inválida, escolha entre 1 a 5: ')

# Função para cadastrar alunos
def cadastrarAluno():
    global ra

    nome = str(input('Qual o nome do aluno? '))
    while nome == "":
        nome = str(input('Digite o nome do aluno? '))

    nota = int(input(f'Digite a nota que {nome} teve: '))

    if nota == "" or nota < 0 or nota > 10:

        while True:
            if nota == "":
                nota = int(input('Este campo não pode ficar vazio: '))
            elif nota < 0 or nota > 10:
                nota = int(input('Digite uma nota entre 0 e 10: '))
            else:
                break
        
    print(f'Aluno {nome} cadastrado com sucesso!')

    ra += 1

    alunos.append({
        "nome": nome,
        "nota": nota,
        "RA": ra
    })

# Função para listar alunos
def listarAlunos():
    for aluno in alunos:
        print(f"RA: {aluno['RA']}, Nome: {aluno['nome']}, Nota: {aluno['nota']}")

# Função para ver a média da turma
def mediaTurma():
    totalNotas = 0
    quantidadeAlunos = 0

    for notas in alunos:
        totalNotas += notas['nota']
        quantidadeAlunos += 1

    media = (totalNotas // quantidadeAlunos)

    print(f'A média da turma é {media}')

# Função para buscar aluno
def buscarAluno():
    print("buscar aluno")

# Chamando função MENU
menu()
