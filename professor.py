import pessoa

class Professor(pessoa.Pessoa):
        def __init__(self,cpf,nome,sobrenome,codigoProfessor):
            super().__init__(cpf,nome,sobrenome)
            self._codigoProfessor = codigoProfessor

        def setCodigoProfessor(self,codigoProfessor):
            self._codigoProfessor = codigoProfessor
       
        def getCodigoProfessor(self):
            return self._codigoProfessor

        def publicarNotas(self):
            print("aqui sera definida a rotina de publicação de notas pelo professor")