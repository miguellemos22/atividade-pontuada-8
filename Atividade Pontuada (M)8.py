import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# Criando conexão com banco de dados.
Session = sessionmaker(bind=MEU_BANCO)
session = Session()


# Criando tabela.

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    # Definindo campos da tabela.
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    idade = Column("idade", String)
    cpf = Column("cpf", String)
    setor = Column("setor", String)
    funcao = Column("funcao", String)
    salario = Column("salario", String)
    telefone = Column("telefone", String)

# Definindo atributos das Classes

    def __init__(self, nome: str, idade: str, cpf: str, setor: str, funcao: str, salario: str, telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.setor = setor
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=MEU_BANCO)
print("""
        escolha uma das opções disponiveis
      
    1 - Adicionar um funcionario
    2 - Consultar um funcionario
    3 - Atualizar os dados de um funcionario
    4 - Excluir um funcionario
    5 - Listar todos os funcionarios
    0 - Sair do sistema.
      
""")
match(Usuario):
    case 1:
        nome = input("digite seu nome: ")
        idade =int(input("digite sua idade: "))
        cpf = int(input("digite seu cpf: "))
        setor = int("digite seu setor: ")
        funcao = input("digite sua função: ")
        salario = input("digite seu salario: ")
        telefone = int(input("digite seu numero de telefone: "))
    case 2:
        


# Salvar no banco de dados.
os.system("cls || clear")        