import pandas as pd

class Escola:
    def __init__(self):
        self._professores = []
        self._alunos = []
        self._aulas = []

    def adicionar_aluno(self, aluno):
       
        nomes_alunos = [a._nome for a in self._alunos]
        if aluno._nome not in nomes_alunos:
            if aluno._aula in self._aulas:
                self._alunos.append(aluno)
                print("Aluno adicionado com sucesso!")
            else:
                print ("Aula não consta no banco de dados!")
        else:
            print(f"'{aluno._nome}' já consta no nosso Banco de Dados. Não foi adicionado novamente.")
       
    def adicionar_professor(self, professor):
        nomes_professores = [p._nome for p in self._professores]
        if professor._nome not in nomes_professores:
            if professor._aula in self._aulas:
                self._alunos.append(professor)
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

        if len(self._alunos) == 0:
            print('Não há alunos matriculados!')
        else:       
            data = {"Nome": [aluno._nome for aluno in self._alunos],
                    "Aula": [aluno._aula for aluno in self._alunos],
                    "Matrícula": [aluno._status_da_matricula for aluno in self._alunos],
                    "Mensalidade": [aluno._mensalidade for aluno in self._alunos]}
            df = pd.DataFrame(data)
            pd.set_option('display.max_columns', None)
            print(df.to_string(index=False))

    def mostrar_professores(self):
        if len(self._professores) == 0:
            print("Não há professores cadastrados!")
        else:
            data = {"Nome": [professor._nome for professor in self._professores],
                    "Aula": [professor._aula for professor in self._professores]}
            df = pd.DataFrame(data)
            pd.set_option('display.max_columns', None)
            print(df.to_string(index=False))
        
    def mostrar_aulas(self):
        if len(self._aulas) == 0:
            print("Não há aulas cadastradas!")
        else:
            data = {"Aula": [aula for aula in self._aulas]}
            df = pd.DataFrame(data)
            pd.set_option('display.max_columns', None)
            print(df.to_string(index=False))

    def matricula_aluno(self, nome):
        for aluno in self._alunos:
            if aluno._nome == nome:
                aluno._status_da_matricula = not aluno._status_da_matricula
                print("Situação da matrícula alterada com sucesso!")
                break
            else:
                print("Aluno não consta no banco de dados!")

class Aluno(Escola):
    def __init__(self, nome, aula, mensalidade):
        self._nome = nome
        self._aula = aula 
        self._mensalidade = mensalidade
        self._status_da_matricula = False
        
    def __str__(self):
        return f'Nome: {self._nome} | Aula: {self._aula} | Matrícula: {self._status_da_matricula} | Mensalidade: {self._mensalidade}'
   
class Professor(Escola):
    def __init__(self, nome, aula, salario):
        self._nome = nome
        self._aula = aula 
        self._salario = salario
        self.adicionar_professor(self)

    def __str__(self):
        return f'Nome: {self._nome} | Aula: {self._aula} | Salario: {self._salario}'


'''escola = Escola()
escola.adicionar_aula('Guitarra')
aluno = Aluno('pedro', 'Guitarra', 120)
escola.adicionar_aluno(aluno)
escola.mostrar_alunos()
escola.matricula_aluno("pedro")
escola.mostrar_alunos()'''