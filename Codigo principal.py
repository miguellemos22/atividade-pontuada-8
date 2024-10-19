import os
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base

""""
Integrantes da equipe: 

- Gabriel Pinto dos santos 
- Miguel LeMOS

"""

# Criando banco de dados.
db = create_engine("sqlite:///meubanco.db")

# Criando conexão com banco de dados.
Session = sessionmaker(bind=db)
session = Session()


# Criando tabela.
Base = declarative_base()

class Funcionario(Base):
    __tablename__ = "funcionario"
    
    nome = Column("nome", String)
    idade = Column("idade", Integer)
    cpf = Column("cpf", Integer, primary_key=True)
    setor = Column("setor", String)
    funcao = Column("funcao", String)
    salario = Column("salario", Float)
    telefone = Column("telefone", Float)
    
    
    def __init__(self, nome , idade, cpf, setor, funcao, salario, telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.setor = setor
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone
        
        
# Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)

os.system("cls || clear")

def limpar_tela():
    os.system("cls || clear")
    
def listar_todos_funcionarios():
    """Lista todos os funcionários cadastrados."""
    funcionarios = session.query(Funcionario).all()

    if funcionarios:
        print("\nLista de Funcionários:\n")
        for funcionario in funcionarios:
            print(f"CPF: {funcionario.cpf} - Nome: {funcionario.nome} - Idade: {funcionario.idade} - Setor: {funcionario.setor} - Função: {funcionario.funcao} - Salário: {funcionario.salario} - Telefone: {funcionario.telefone}")
    else:
        print("Não há funcionários cadastrados.")

def menu():
    print("="*40)
    print(f"{"RH System":^40}")
    print("="*40)
    print("""
    1 - Adicionar um funcionário
    2 - Consultar um funcionário
    3 - Atualizar os dados de um funcionário
    4 - Excluir um funcionário 
    5 - Listar todos os funcionários
    0 - Sair do sistema.     
          """)


while True:
    lista_funcionario = []
    menu()
    opcao = input("digite seu numero: ")
    match opcao:
        case "1": 
            nome = input("Digite seu nome: ")
            idade = int(input("Digite sua idade: "))
            cpf_usuario = int(input("Digite seu CPF: "))
            setor = input("Digite seu setor: ")
            funcao = input("Digite sua função: ")
            salario = float(input("Digite seu salario: "))
            telefone = int(input("Digite seu telefone: "))
            
            funcionario = Funcionario(nome=nome, idade=idade, cpf=cpf_usuario, setor=setor, funcao=funcao, salario=salario, telefone=telefone)
            session.add(funcionario)
            session.commit()
            limpar_tela()


        case "2":  # Consultar funcionário
            cpf_usuario = int(input("Coloque o CPF: "))
            funcionario = session.query(Funcionario).filter_by(cpf=cpf_usuario).first()  # Obtém o primeiro funcionário com o CPF
    
            if funcionario:  # Verifica se encontrou o funcionário
                print(f"CPF: {funcionario.cpf} - Nome: {funcionario.nome} - Idade: {funcionario.idade} - Setor: {funcionario.setor} - Função: {funcionario.funcao} - Salário: {funcionario.salario} - Telefone: {funcionario.telefone}")
            else:
                print(f"Funcionário com CPF {cpf_usuario} não encontrado.")

            input("Pressione Enter para continuar...")


        case "3":
            cpf_usuario = int(input("Digite o CPF: "))
            funcionario = session.query(Funcionario).filter_by(cpf=cpf_usuario).first()

            if funcionario:
                funcionario.nome = input("Digite seu nome: ")
                funcionario.idade = int(input("Digite sua idade: "))
                funcionario.setor = input("Digite seu setor: ")
                funcionario.funcao = input("Digite sua função: ")
                funcionario.salario = float(input("Digite seu salario: "))
                funcionario.telefone = int(input("Digite seu telefone: "))
                session.commit()
                print("Usuário atualizado.")
            else:
                print(f"Funcionário com CPF {cpf_usuario} não encontrado.")
            
        case "4":
            cpf_usuario = int(input("Digite o CPF: "))
            funcionario = session.query(Funcionario).filter_by(cpf = cpf_usuario).first()
            session.delete(funcionario)
            session.commit()
            print("Usuário deletado.")
            limpar_tela()
            
        case "5":
            listar_todos_funcionarios()
            input("Pressione Enter para continuar...")
        case "0":
            break

            
            
        
    


        
    