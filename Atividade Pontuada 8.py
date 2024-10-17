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
    __tablename__ = "funcionarios"

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

# Salvar no banco de dados.
os.system("cls || clear")


# Funções CRUD
def create_funcionario(session, nome, idade, cpf, setor, funcao, salario, telefone):
    novo_funcionario = funcionario(nome=nome, idade=idade, cpf=cpf, setor=setor, funcao=funcao, salario=salario, telefone=telefone)
    session.add(novo_funcionario)
    session.commit()

def salvar_funcionario(session, funcionario_id):
    funcionario = session.query(funcionario).filter_by(id=funcionario_id).first()
    if funcionario:
        print(funcionario)
    else:
        print("Funcionário não encontrado.")

def listar_todos_funcionarios(session, funcionario_id, **kwargs):
    session.query(funcionario).filter_by(id=funcionario_id).update(kwargs)
    session.commit()

def pesquisar_um_funcionario(session, funcionario_id):
    session.query(funcionario).filter_by(id=funcionario_id).delete()
    session.commit()

# Função para listar todos os funcionários
def atualizar_funcionario(session):
    funcionarios = session.query(funcionario).all()
    for funcionario in funcionarios:
        print(funcionario)







#Função principal
def main():
    Session = sessionmaker(bind= MEU_BANCO)
    session = Session()

    while True:
        print("\n=== RH System ===")
        print("1 - Adicionar um funcionário")
        print("2 - Consultar um funcionário")
        print("3 - Atualizar os dados de um funcionário")
        print("4 - Excluir um funcionário")
        print("5 - Listar todos os funcionários")
        print("0 - Sair do sistema.")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            # Lógica para adicionar um funcionário
            nome = input("Nome: ")
            # ... outros dados
            create_funcionario(session, nome, ...)
        elif opcao == 2:
            # Lógica para consultar um funcionário
            funcionario_id = int(input("Digite o ID do funcionário: "))
            read_funcionario(session, funcionario_id)
        # ... outras opções

        if opcao == 0:
            break

if __name__ == "__main__":
    main()
