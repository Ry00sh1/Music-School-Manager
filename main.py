from classes import Escola, Aluno, Professor
import os

# Criando uma instância da classe Escola
lacord = Escola()
lacord.adicionar_aula('Guitarra')

def main():
    ''' Essa função é responsável por limpar a tela e imprimir uma mensagem de boas vindas
    
    Outputs:
    - Mensagem de boas vindas ao sistema

    '''
    os.system('cls')
    print('Boas vindas ao sistema de gestão da Escola de Música Sustenido\n\n')
    menu()

def menu():
    
    print('''Escolha uma opção:
1 - Gestão de alunos
2 - Gestão de professores
3 - Gestão de aulas''')
    
    try:
        opcao = int(input('Opção: '))
        if opcao == 1:
            menu_aluno()
        elif opcao == 2:
            menu_professor()    
        elif opcao == 3:
            menu_aula()
        else:
            print('Opção inválida, tente novamente.\n')
            os.system('cls')        
            main()
      
    except:
        print('Opção inválida, tente novamente.\n')
        os.system('cls')        
        main()

def retorna():
    input("\nDigite uma tecla para voltar ao menu\n")
    main()

def menu_aluno():

    ''' Essa função é responsável por criar um menu para o usuário escolher entre listar ou adicionar um aluno ao banco de dados
        
    Inputs:
    - Opção para entrar na função de listagem dos alunos

    Outputs:
    - Opção para entrar na função de adicionar um novo aluno

    '''

    os.system('cls') 
    print('''Gestão de alunos
1 - Listar
2 - Adicionar
3 - Alterar a situação da matrícula\n''')
    
    try:
        opcao = int(input('Opção: '))
        if opcao == 1:
            lacord.mostrar_alunos()
            retorna()
        elif opcao == 2:
            adicionar_aluno()
        elif opcao == 3:
            matricula_aluno()
        else:
            print('Opção inválida, tente novamente.\n')
            os.system('cls')        
            menu_aluno()
      
    except:
        print('Opção inválida, tente novamente.\n')
        os.system('cls')        
        menu_aluno()

def menu_professor():
    os.system('cls') 
    print('''Gestão de professores
1 - Listar
2 - Adicionar\n''')

    try:
        opcao = int(input('Opção: '))
        if opcao == 1:
            lacord.mostrar_professores()
            retorna()
        elif opcao == 2:
            adicionar_professor()
        else:
            print('Opção inválida, tente novamente.\n')
            os.system('cls')        
            menu_professor()
      
    except:
        print('Opção inválida, tente novamente.\n')
        os.system('cls')        
        menu_professor()

def menu_aula():
    os.system('cls') 
    print('''Gestão de aulas
1 - Listar
2 - Adicionar\n''')
    
    try:
        opcao = int(input('Opção: '))
        if opcao == 1:
            lacord.mostrar_aulas()
            retorna()
        elif opcao == 2:
            adicionar_aula()
        else:
            print('Opção inválida, tente novamente.\n')
            os.system('cls')        
            menu_aula()
      
    except:
        print('Opção inválida, tente novamente.\n')
        os.system('cls')        
        menu_aula()

def adicionar_aluno():
    nome = input('Digite o nome do aluno:\n')
    aula = input('Digite a aula que esse aluno frequenta:\n')
    mensalidade = float(input('Digite o valor da mensalidade:\nR$ '))
    aluno = (Aluno(nome, aula, mensalidade))
    lacord.adicionar_aluno(aluno)
    retorna()

def adicionar_professor():
    nome = input('Digite o nome do professor:\n')
    aula = input('Digite a aula que esse professor leciona:\n')
    salario = float(input('Digite o valor do salário desse professor:\nR$ '))
    professor = (Professor(nome, aula, salario))
    lacord.adicionar_professor(professor)
    retorna()

def adicionar_aula():
    aula = input("Digite a aula a ser adicionada:\n")
    lacord.adicionar_aula(aula)
    retorna()

def matricula_aluno():
    aluno = input("Digite o nome do aluno que terá o status da matrícula alterado:\n")
    lacord.matricula_aluno(aluno)
    retorna()

if __name__ == '__main__':
    main()