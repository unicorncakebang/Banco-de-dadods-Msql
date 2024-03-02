#importando o banco de dados
import sqlite3

Banco = sqlite3.connect("Banco.db")

cursor = Banco.cursor()

#classe aluno
class aluno():
def __init__(self,nome,cpf,nascimento,nacionalidade)
    self.nome = nome
    self.cpf = cpf
    self.nascimento = nascimento
    self.nacionalidade = nacionalidade

def comprovante(m):
  print("Nome do aluno:"+nome.m)
  print("CPF do alunos:"+cpf.m)
  print("Data de nascimento"+nascimento.m)
  print("Nacionalidade do aluno"+nacionalidade.m)


#criando a tabela de aluno do banco de dados
cursor.execute("CREATE TABLE Aluno(nome text , cpf text ,nascimento text,nacionalidade text)")


# entrada de informações
x = input("nome do aluno:")
y = input("cpf:")
z = input("data de nascimento:")
p = input("nacionalidade:")

#fazendo a concatenação com o banco de dados

for registro =tabela['nome']
    registro = str(x)

for identidade = tabela['cpf']
    identidade = str(y)

for nascimento = tabela['nascimento']
    nascimento = str(z)

for local = tabela['nacionalidade']
    local = str(p)


#fazendo a inserção dos dados no banco de dados

cursor.execute("INSERT INTO Aluno VALUES('"+nome+"','"+cpf+"','"+nascimento+"','"+nacionalidade+"')")
banco.commit()

#mostrando a banco de dados
cursor.execute("SELECT * FROM Aluno")
print(cursor.fetchall())


#mostrando
 H = aluno(x,y,z,p)
 H.comprovante
