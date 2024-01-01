import os
import pandas as pd



professores = []
aulas = []



class Aluno:

    alunos = []

    def __init__(self, nome, aula, mensalidade):
        self._nome = nome
        self._aula = aula
        self._mensalidade = mensalidade
        self._status_da_matricula = False

    '''def __str__(self):
        return f'Nome: {self.nome}, Aula: {self.aula}, Matricula: {self.status_da_matricula}, Mensalidade: {self.mensalidade}'''
    
    @classmethod
    def listar_alunos(cls):
        print(f'{'Nome do aluno'.ljust(25)} | {'Aula'.ljust(25)} | {'Mensalidade'.ljust(25)} |{'Matrícula'}')
        for aluno in cls.restaurantes:
            print(f'{aluno._nome.ljust(25)} | {aluno._aula.ljust(25)} | {str(aluno._mensalidade).ljust(25)} |{aluno._status_da_matricula}')

class Professor:
    def __init__(self, nome, aula):
        self.nome = nome
        self.aula = aula

    '''def __str__(self):
        return f'Nome: {self.nome}, Aula:{self.aula}'''



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

    ''' Essa função é responsável por criar um menu para o usuário escolher entre listar ou adicionar um aluno ao banco de dados
        
    Inputs:
    - Opção para entrar na função de listagem dos alunos

    Outputs:
    - Opção para entrar na função de adicionar um novo aluno

    '''

    os.system('cls') 
    print('''Listar ou adicionar alunos
1 - Listar
2 - Adicionar\n''')
    
    try:
        opcao = int(input('Opção: '))
        if opcao == 1:
            listar(alunos)
        elif opcao == 2:
            adicionarAluno()
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
    #[print(f"{indice+1} - {valor}") for indice, valor in enumerate(lista)] if len(lista) > 0 else print("Lista vazia!")
    
    # Cria uma lista de dicionários representando os alunos
    dados_alunos = [
    {
        'Nome': aluno.nome,
        'Aula': aluno.aula,
        'Matricula': aluno.status_da_matricula,
        'Mensalidade': aluno.mensalidade
    }
    for aluno in alunos
    ]

    # Cria o DataFrame
    tabela_alunos = pd.DataFrame(dados_alunos)  
    
    # Verifica se a tabela está vazia antes de imprimir
    if not tabela_alunos.empty:
        pd.set_option('display.colheader_justify', 'center')  # Alinhar os cabeçalhos das colunas ao centro
        print(tabela_alunos)
    else:
        print("A lista está vazia.")

    retorna()

def adicionarAluno():
    nome = input('Digite o nome do aluno:\n')
    aula = input('Digite a aula que esse aluno frequenta:\n')
    mensalidade = float(input('Digite o valor da mensalidade:\nR$ '))
    aluno = (Aluno(nome, aula, mensalidade))
    alunos.append(aluno)
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


class Aluno:
    def __init__(self, nome, aula, mensalidade, status_da_matricula = False):
        self.nome = nome
        self.aula = aula
        self.mensalidade = mensalidade
        self.status_da_matricula = status_da_matricula

    '''def __str__(self):
        return f'Nome: {self.nome}, Aula: {self.aula}, Matricula: {self.status_da_matricula}, Mensalidade: {self.mensalidade}'''

class professor(escola):
    def __init__(self, nome, funcao, diasDeAula, contrato, salario):
        super().__init__(nome, funcao, diasDeAula, contrato, salario)
        self.funcao = professor
"""