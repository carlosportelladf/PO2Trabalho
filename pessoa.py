class Pessoa:
        def __init__(self,cpf,nome,sobrenome):
            self._cpf = cpf
            self._nome = nome
            self._sobrenome = sobrenome

        def setCpf(self,cpf):
            self._cpf = cpf

        def setNome(self,nome):
            self._nome = nome

        def setSobrenome(self,sobrenome):
            self._sobrenome = sobrenome

        def getCpf(self):
            return self._cpf

        def getNome(self):
            return self._nome

        def getSobrenome(self):
            return self._sobrenome
        
        def getNomeCompleto(self):
            return self._nome + " " + self._sobrenome


    
    

            