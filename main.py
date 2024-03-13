from classes import Escola, Aluno, Professor
import os

# Criando uma instância da classe Escola
sustenido = Escola()
sustenido.adicionar_aula('Guitarra')
aluno = (Aluno('Pedro', 'Guitarra', 120))
sustenido.adicionar_aluno(aluno)

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
    input("\nAperte uma tecla para voltar ao menu\n")
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
3 - Alterar informações
4 - Remover aluno\n''')
    
    try:
        opcao = int(input('Opção: '))
        if opcao == 1:
            sustenido.listar_alunos()
            retorna()
        elif opcao == 2:
            adiciona_aluno()
        elif opcao == 3:
            altera_aluno()
        elif opcao == 4:
            remove_aluno()
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
        while opcao != 1 or opcao != 2:
            if opcao == 1:
                sustenido.mostrar_professores()
                retorna()
            elif opcao == 2:
                adiciona_professor()
            else:
                menu_professor()
                print('Opção inválida, tente novamente.\n')
                    
                
        
    except:
        menu_professor()
        print('Opção inválida, tente novamente.\n')
            
        
    
        

def menu_aula():
    os.system('cls') 
    print('''Gestão de aulas
1 - Listar
2 - Adicionar\n''')
    
    try:
        opcao = int(input('Opção: '))
        if opcao == 1:
            sustenido.mostrar_aulas()
            retorna()
        elif opcao == 2:
            adiciona_aula()
        else:
            print('Opção inválida, tente novamente.\n')
                
            menu_aula()
      
    except:
        print('Opção inválida, tente novamente.\n')
            
        menu_aula()

def adiciona_aluno():
    nome = input('Digite o nome do aluno:\n')
    aula = input('Digite a aula que esse aluno frequenta:\n')
    mensalidade = float(input('Digite o valor da mensalidade:\nR$ '))
    aluno = (Aluno(nome, aula, mensalidade))
    sustenido.adicionar_aluno(aluno)
    retorna()

def remove_aluno():
    aluno = input("Digite o nome do aluno que será removido do Banco de Dados:\n")
    sustenido.excluir_aluno(aluno)
    retorna()

def adiciona_professor():
    nome = input('Digite o nome do professor:\n')
    aula = input('Digite a aula que esse professor leciona:\n')
    salario = float(input('Digite o valor do salário desse professor:\nR$ '))
    professor = (Professor(nome, aula, salario))
    sustenido.adicionar_professor(professor)
    retorna()

def adiciona_aula():
    aula = input("Digite a aula a ser adicionada:\n")
    sustenido.adicionar_aula(aula)
    retorna()

def altera_aluno():
    
    print('''Alterar:
1 - Nome
2 - Mensalidade
3 - Matrícula
4 - Aula\n''')
    
    opcao = int(input('Opção: '))
    try:
        
        print(sustenido.functions_aluno(opcao))
        retorna()
      
    except Exception as e:
        
        os.system('cls')    
        print(f'Erro: {e}\nOpção inválida, tente novamente.\n')     
        altera_aluno()

    

if __name__ == '__main__':
    main()