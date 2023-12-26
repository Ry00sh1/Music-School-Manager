import os

alunos = []
professores = []
aulas = []

def main():
    os.system('cls')
    print('Boas vindas ao sistema de gestão da Escola de Música Sustenido\n\n')
    menu()

def menu():
    
    print('''Escolha uma opção:
1 - Listar ou adicionar alunos
2 - Listar ou adicionar professores
3 - Listar ou adicionar aulas''')
    
    try:
        opcao = int(input('Opção: '))
        if opcao == 1:
            listOrAddAluno()
        elif opcao == 2:
            listOrAddProfessor()    
        elif opcao == 3:
            listOrAddAulas()
        else:
            print('Opção inválida, tente novamente.\n')
            os.system('cls')        
            main()
      
    except:
        print('Opção inválida, tente novamente.\n')
        os.system('cls')        
        main()

def retorna():
    input("\nDigite uma tecla para voltar ao menus\n")
    main()

def listOrAddAluno():
    os.system('cls') 
    print('''Listar ou adicionar alunos
1 - Listar
2 - Adicionar\n''')
    
    try:
        opcao = int(input('Opção: '))
        if opcao == 1:
            listar(alunos)
        elif opcao == 2:
            nome = input('Digite o nome do aluno:\n')
            adicionar(alunos, nome)
        else:
            print('Opção inválida, tente novamente.\n')
            os.system('cls')        
            listOrAddAluno()
      
    except:
        print('Opção inválida, tente novamente.\n')
        os.system('cls')        
        listOrAddAluno()

def listOrAddProfessor():
    os.system('cls') 
    print('''Listar ou adicionar professores
1 - Listar
2 - Adicionar\n''')

    try:
        opcao = int(input('Opção: '))
        if opcao == 1:
            listar(professores)
        elif opcao == 2:
            nome = input('Digite o nome do professor:\n')
            adicionar(professores, nome)
        else:
            print('Opção inválida, tente novamente.\n')
            os.system('cls')        
            listOrAddAluno()
      
    except:
        print('Opção inválida, tente novamente.\n')
        os.system('cls')        
        listOrAddAluno()

def listOrAddAulas():
    os.system('cls') 
    print('''Listar ou adicionar aulas
1 - Listar
2 - Adicionar\n''')
    
    try:
        opcao = int(input('Opção: '))
        if opcao == 1:
            listar(aulas)
        elif opcao == 2:
            aula = input('Digite a aula que quer adicionar:\n')
            adicionar(aulas, aula)
        else:
            print('Opção inválida, tente novamente.\n')
            os.system('cls')        
            listOrAddAluno()
      
    except:
        print('Opção inválida, tente novamente.\n')
        os.system('cls')        
        listOrAddAluno()

def listar(lista):
    [print(f"{indice+1} - {valor}") for indice, valor in enumerate(lista)] if len(lista) > 0 else print("Lista vazia!")
    
    retorna()

def adicionar(lista, item):
    lista.append(item)
    retorna()

if __name__ == '__main__':
    main()




"""class escola:
    def __init__(self, nome, funcao, diasDeAula, mensalidade, contrato, aula, salario):
        self.nome = nome
        self.funcao = funcao
        self.diasDeAula = diasDeAula
        self.mensalidade = mensalidade
        self.contrato = contrato
        self.aula = aula
        self.salario = salario


class aluno(escola):
    def __init__(self, nome, diasDeAula, mensalidade, contrato, aula):
        super().__init__(nome,diasDeAula, mensalidade, contrato, aula)
        self.funcao = aluno

class professor(escola):
    def __init__(self, nome, funcao, diasDeAula, contrato, salario):
        super().__init__(nome, funcao, diasDeAula, contrato, salario)
        self.funcao = professor
"""