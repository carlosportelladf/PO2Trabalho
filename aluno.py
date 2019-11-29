import pessoa

class Aluno(pessoa.Pessoa):
        def __init__(self,cpf,nome,sobrenome,matricula):
            super().__init__(cpf,nome,sobrenome)
            self._matricula = matricula

        def setMatricula(self,matricula):
            self._matricula = matricula
       
        def getMatricula(self):
            return self._matricula

        
        def registrarPresenca(self):
             print ("Ainda não implementado a rotina de registro de presenças do aluno")
             
