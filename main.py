import sqlite3
from sqlite3 import Error
from time import sleep
import schema
import tabelas
from cores import Cores

def menu():
	print(20 * '*')
	print(f"{Cores.BOLD}{Cores.OKBLUE}***-- Menu de Opções --**{Cores.ENDC}")
	print(20 * '*')
	print(f"{Cores.BOLD}1. Camping")
	print("2. Endereço")
	print("3. Infraestrutura")
	print("4. Acomodação")
	print(f"5. Preço{Cores.ENDC}")
	print(f"{Cores.BOLD}{Cores.FAIL}6. Sair{Cores.ENDC}")
	print(20 * '*')
	selecao = int(input('Selecione uma opcão: '))
	return selecao

def submenu(tabela):
	print(20 * '*')
	print(f"{Cores.BOLD}{Cores.OKBLUE}*** Opção {tabela} ***{Cores.ENDC}")
	print(20 * '*')
	print(f"{Cores.BOLD}{Cores.FAIL}0. Retorna ao menu principal{Cores.ENDC}")
	print(f"{Cores.BOLD}1. Inserir {tabela}")
	print(f"2. Atualizar {tabela}")
	print(f"3. Pesquisar {tabela}")
	print(f"4. Pesquisar Único {tabela}")
	print(f"5. Excluir {tabela}{Cores.ENDC}")
	print(20 * '*')
	opcaosub = int(input('Selecione uma opcão: '))
	return opcaosub

def criar_conexao(banco):
	conn = None
	try:
		conn = sqlite3.connect(banco)
		print(sqlite3.sqlite_version)
		return conn
	except Error as e:
		print(e)

def limpar():
    import os
    from time import sleep
    
    def screen_clear():
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            _ = os.system('cls')
    sleep(1)
    screen_clear()

if __name__ == '__main__':
	limpar()
	print(20 * '*')
	print(f"{Cores.BOLD}{Cores.OKBLUE}***-- Projeto --***{Cores.ENDC}")
	print(20 * '*')
	print(f"{Cores.BOLD}{Cores.OKBLUE}Criando o banco de dados se não existir ...{Cores.ENDC}") 
	banco = input("Informe o nome do banco a ser criado: ")
	print(f"{Cores.BOLD}{Cores.OKBLUE}Criando conexão ...{Cores.ENDC}")
	conn = criar_conexao(banco)
	print(f"{Cores.BOLD}{Cores.OKBLUE}Criando tabelas do banco de dados se não existirem ...{Cores.ENDC}")
	schema.criar_tabelas(banco)
	sleep(2)
	input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")
	limpar()
	opcao = menu()
	limpar()

	while opcao != 6:
		if opcao == 1:
			tabela = 'camping'
		elif opcao == 2:
			tabela = 'endereco'
		elif opcao == 3:
			tabela = 'infraestrutura'
		elif opcao == 4:
			tabela = 'acomodacao'  
		elif opcao == 5:
			tabela = 'preco'
		else:
			print('Opção inválida!')

		opcaosub = submenu(tabela)
		limpar()
		while opcaosub != 0:
			if opcaosub == 1:
				print(f"Inserir {tabela}")
				tabelas.inserir(tabela, conn)
			elif opcaosub == 2:
				print(f"Atualizar {tabela}")
				tabelas.atualizar(tabela, conn)
			elif opcaosub == 3:
				print(f"Pesquisar {tabela}")
				tabelas.pesquisar(tabela, conn)
			elif opcaosub == 4:
				print(f"Pesquisar único {tabela}")
				tabelas.pesquisarUnico(tabela, conn)
			elif opcaosub == 5:
				print(f"Excluir {tabela}")
				tabelas.excluir(tabela, conn)
			else:
				print('Opção inválida!')
			limpar()
			opcaosub = submenu(tabela)
			limpar()
		opcao = menu()
		limpar()