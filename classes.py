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

    def mostrar_alunos(self):
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

    def matricula_aluno(self, nome):
        for aluno in self._alunos:
            if aluno._nome == nome:
                aluno._status_da_matricula = not aluno._status_da_matricula
                print("Situação da matrícula alterada com sucesso!")
                break
        else:
            print("Aluno não consta no banco de dados!")

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
        return self._mensalidade

    @property
    def status_da_matricula(self):
        if self._status_da_matricula:
            return 'Ativada'
        else:
            return 'Desativada'

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




