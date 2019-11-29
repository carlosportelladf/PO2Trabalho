import pessoa, aluno, professor

# instancia a classe pessoa
pessoa = pessoa.Pessoa(123,"Joao Carlos","da Silva")
# instancia a classe aluno
aluno = aluno.Aluno(123,"Carlos","Portella",12)
# instancia a classe professor
professor = professor.Professor(123,"Allan","Paulo",20)

#mostra diversas informações das classes instanciadas
print ("A classe pessoa foi instanciada com o cpf ", pessoa.getCpf())
print ("O nome completo do professor instanciado é " , professor.getNomeCompleto())
print ("O aluno instanciado é", aluno.getNomeCompleto(), "com a matricula nr. ", aluno.getMatricula())
print ("O professor ", professor.getNomeCompleto(), "possui o código  ", professor.getCodigoProfessor())

#chamada de metodos das classes aluno e professor
professor.publicarNotas()
aluno.registrarPresenca()