from tabulate import tabulate

class Escola:
    def __init__(self):
        self._professores = []
        self._alunos = []
        self._aulas = []

    def adicionar_aluno(self, aluno):
        nomes_alunos = [a.nome for a in self._alunos]
        if aluno.nome not in nomes_alunos:
            if aluno.aula in self._aulas:
                self._alunos.append(aluno)
                print("Aluno adicionado com sucesso!")
            else:
                print("Aula não consta no banco de dados!")
        else:
            print(f"'{aluno.nome}' já consta no nosso Banco de Dados. Não foi adicionado novamente.")

    def listar_alunos(self):
        if not self._alunos:
            print('Não há alunos matriculados!')
        else:
            data = {
                "Nome": [aluno.nome for aluno in self._alunos],
                "Aula": [aluno.aula for aluno in self._alunos],
                "Matrícula": [aluno.status_da_matricula for aluno in self._alunos],
                "Mensalidade": [aluno.mensalidade for aluno in self._alunos]
            }
            table = tabulate(data, headers='keys', tablefmt='simple')
            print(table)

    def functions_aluno(self, opcao):
        nome = input('Qual o nome atual do aluno?\n ')
        for aluno in self._alunos:
            if aluno._nome == nome:
                if opcao == 1:
                    novo_nome = input('Digite o nome atualizado: ')
                    aluno._nome = novo_nome
                    if aluno._nome == novo_nome:
                        return f"'Nome alterado de {nome} para {aluno._nome}'."
                    return 'Falha ao alterar o nome do aluno. Tente novamente'
                    
                if opcao == 2:
                    mensalidade_antiga = aluno._mensalidade
                    nova_mensalidade = float(input('Digite o valor da mensalidade atualizado: '))
                    aluno._mensalidade = nova_mensalidade
                    if aluno._mensalidade == nova_mensalidade:
                        return f"'Valor alterado de R${mensalidade_antiga:.2f} para R${aluno._mensalidade:.2f}'."
                    return 'Falha ao alterar o valor da mensalidade. Tente novamente'
            
                if opcao == 3:
                    aluno._status_da_matricula = not aluno._status_da_matricula
                    return f'Matricula alterada com sucesso'
                
                if opcao == 4:        
                    self._alunos.remove(aluno)
                    return f'{aluno._nome} excluído com sucesso.'
        
        return f"'{aluno._nome}' não consta no nosso Banco de Dados."
        
    def adicionar_professor(self, professor):
        nomes_professores = [p._nome for p in self._professores]
        if professor._nome not in nomes_professores:
            if professor._aula in self._aulas:
                self._professores.append(professor)
                print("Professor adicionado com sucesso!")
            else:
                print ("Aula não consta no banco de dados!")
        else:
            print(f"'{professor._nome}' já consta no nosso Banco de Dados. Não foi adicionado novamente.")

    def adicionar_aula(self, aula):
        if aula not in self._aulas:
            self._aulas.append(aula)
        else:
            print(f"Aula '{aula}' já consta no banco de dados!")
  
    def mostrar_professores(self):
        if not self._professores:
            print("Não há professores cadastrados!")
        else:
            data = {
                "Nome": [professor.nome for professor in self._professores],
                "Aula": [", ".join(professor.aula) if isinstance(professor.aula, list) else professor.aula for professor in self._professores],
                "Salário": [f"R$ {professor.salario:.2f}" for professor in self._professores]
            }
            table = tabulate(data, headers='keys', tablefmt='simple')
            print(table)

    def mostrar_aulas(self):
        if len(self._aulas) == 0:
            print("Não há aulas cadastradas!")
        else:
            data = {"Aula": [aula for aula in self._aulas]}
            table = tabulate(data, headers='keys', tablefmt='simple')
            print(table)

    

class Pessoa:
    def __init__(self, nome, aula):
        self._nome = nome
        self._aula = aula

    @property
    def nome(self):
        return self._nome

    @property
    def aula(self):
        return self._aula

class Aluno(Pessoa):
    def __init__(self, nome, aula, mensalidade):
        super().__init__(nome, aula)
        self._mensalidade = mensalidade
        self._status_da_matricula = False

    @property
    def mensalidade(self):
        return f'R$ {self._mensalidade:.2f}'

    @property
    def status_da_matricula(self):
        return 'Ativada' if self._status_da_matricula else 'Desativada'
    
    @Pessoa.aula.setter
    def aula(self, nova_aula):
        self._aula = nova_aula

    def __str__(self):
        return f'Nome: {self._nome} | Aula: {self._aula} | Matrícula: {self._status_da_matricula} | Mensalidade: {self._mensalidade}'

class Professor(Pessoa):
    def __init__(self, nome, aula, salario):
        super().__init__(nome, aula)
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    @Pessoa.aula.setter
    def aula(self, nova_aula):
        if isinstance(nova_aula, list):
            self._aula = nova_aula
        else:
            print("Aula para Professor deve ser uma lista de aulas.")

    def adicionar_aula(self, aula):
        if isinstance(aula, list):
            self._aula.extend(aula)
        else:
            print("Aula para Professor deve ser uma lista de aulas.")

    def __str__(self):
        return f'Nome: {self._nome} | Aula: {self._aula} | Salário: {self._salario}'




