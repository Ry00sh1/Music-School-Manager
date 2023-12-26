import os
import datetime

alunos = []
professores = []
aulas = ['Guitarra', 'Violão', 'Bateria', 'Teclado']
def menu():
    
    print('''Escolha uma opção:
1 - Listar ou adicionar alunos
2 - Listar ou adicionar professores
3 - Listar ou adicionar aulas''')
    try:
        opcao = int(input('Opção: '))
        if 1 >= opcao <= 3:
            match opcao:
                case 1:
                    listOrAddAluno()
                case 2:
                    listOrAddProfessor()
                case 3:
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
    input("Digite uma tecla para voltar ao menus\n")
    main()

def listOrAddAluno():
    os.system('cls') 
    print('''Listar ou adicionar alunos
1 - Listar
2 - Adicionar\n''')
    
    try:
        opcao = int(input('Opção: '))
        if 1 >= opcao <= 2:
            match opcao:
                case 1:
                    print(alunos) if len(alunos) > 0 else print("Não há alunos matriculados")
                    retorna()

                case 2:
                    listOrAddProfessor()
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

def listOrAddAulas():
    os.system('cls') 
    print('''Listar ou adicionar aulas
1 - Listar
2 - Adicionar\n''')



def main():
    os.system('cls')
    print('Boas vindas ao sistema de gestão da Escola de Música Sustenido\n\n')
    menu()

if __name__ == '__main__':
    main()




class escola:
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