from cores import Cores

def inserir(tabela, conn):

	c = conn.cursor()

	if tabela == 'camping':
		descricao = input("Descricao: ").title()
		nome = input("Nome: ").title()
		camp = (descricao, nome)
		c.execute("INSERT INTO camping (descricao, nome) VALUES (?,?);", camp)
		conn.commit()
	elif tabela == 'endereco':
		logradouro = input("Rua: ").title()
		numero = int(input("Número: "))
		complemento = input("Complemento: ").title()
		idCamping = int(input("Informe o id (camping) deste endereço: "))
		end = (logradouro, numero, complemento, idCamping)
		c.execute("INSERT INTO endereco (logradouro, numero, complemento, idCamping) VALUES (?,?,?,?);", end)
		conn.commit()
	elif tabela == 'infraestrutura':
		descricao = input("Descrição: ").title()
		idCamping = int(input("Informe o id (camping) desta infraestrutura: "))
		infra = (descricao, idCamping)
		c.execute("INSERT INTO infraestrutura (descricao, idCamping) VALUES (?,?);", infra)
		conn.commit()
	elif tabela == 'acomodacao':
		numero = int(input("Número: "))
		descricao = input("Descrição: ").title()
		qtdPessoas = int(input("Acomoda quantas pessoas: "))
		idCamping = int(input("Informe o id (camping) desta acomodação: "))
		acomodacao = (numero, descricao, qtdPessoas, idCamping)
		c.execute("INSERT INTO acomodacao (numero, descricao, qtdPessoas, idCamping) VALUES (?,?,?,?);", acomodacao)
		conn.commit()
	elif tabela == 'preco':
		valor = int(input("Valor: "))
		descricao = input("Descrição: ").title()
		idAcomodacao = int(input("Informe o id (acomodação) deste preço: "))
		preco = (valor, descricao, idAcomodacao)
		c.execute("INSERT INTO preco (valor, descricao, idAcomodacao) VALUES (?,?,?);", preco)
		conn.commit()

	print(f"{Cores.BOLD}{Cores.OKGREEN}Inserção com sucesso em {tabela}.{Cores.ENDC}")

def atualizar(tabela, conn):

	c = conn.cursor()

	if tabela == 'camping':
		pesquisar(tabela, conn)
		x = input("Indique o id a atualizar: ")
		descricao = input("Descricao: ").title()
		nome = input("Nome: ").title()
		values = (descricao, nome, x)
		c.execute("UPDATE camping SET descricao=?, nome=? WHERE id=?;", values)
		conn.commit()
	elif tabela == 'endereco':
		pesquisar(tabela, conn)
		x = input("Indique o id a atualizar: ")
		logradouro = input("Rua: ").title()
		numero = int(input("Número: "))
		complemento = input("Complemento: ").title()
		values = (logradouro, numero, complemento, x)
		c.execute("UPDATE endereco SET logradouro=?, numero=?, complemento=? WHERE id=?;", values)
		conn.commit()
	elif tabela == 'infraestrutura':
		pesquisar(tabela, conn)
		x = input("Indique o id a atualizar: ")
		descricao = input("Descricao: ").title()
		values = (descricao, x)
		c.execute("UPDATE infraestrutura SET descricao=? WHERE id=?;", values)
		conn.commit()
	elif tabela == 'acomodacao':
		pesquisar(tabela, conn)
		x = input("Indique o id a atualizar: ")
		numero = int(input("Número: "))
		descricao = input("Descricao: ").title()
		qtdPessoas = int(input("Acomoda quantas pessoas: "))
		values = (numero, descricao, qtdPessoas, x)
		c.execute("UPDATE acomodacao SET numero=?, descricao=?, qtdPessoas=? WHERE id=?;", values)
		conn.commit()
	elif tabela == 'preco':
		pesquisar(tabela, conn)
		x = input("Indique o id a atualizar: ")
		valor = int(input("Valor: "))
		descricao = input("Descrição: ").title()
		values = (valor, descricao, x)
		c.execute("UPDATE preco SET valor=?, descricao=? WHERE id=?;", values)
		conn.commit()

	print(f"{Cores.BOLD}{Cores.OKGREEN}Atualização com sucesso em {tabela}.{Cores.ENDC}")
	input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")

def pesquisar(tabela, conn):

	c = conn.cursor()

	if tabela == 'camping':
		c.execute("SELECT * FROM camping;")
		resultado = c.fetchall()
		if resultado:
			print(f'{Cores.BOLD}{Cores.HEADER}ID \tDescricao \tNome {Cores.ENDC}')
			for item in range(len(resultado)):
				print(f'{resultado[item][0]}  \t{resultado[item][1]}   \t{resultado[item][2]}')
		else:
			print(f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")
	elif tabela == 'endereco':
		c.execute("SELECT * FROM endereco INNER JOIN camping ON camping.id = idcamping;")
		resultado = c.fetchall()
		if resultado:
			print(f'{Cores.BOLD}{Cores.HEADER}ID \tLogradouro \tNumero \tComplemento \tIdCamping {Cores.ENDC}')
			for item in range(len(resultado)):
				print(f'{resultado[item][0]}  \t{resultado[item][1]}   \t{resultado[item][2]}   \t{resultado[item][3]}    \t{resultado[item][4]}')
		else:
			print(f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")
	elif tabela == 'infraestrutura':
		c.execute("SELECT * FROM infraestrutura INNER JOIN camping ON camping.id = idCamping;")
		resultado = c.fetchall()
		if resultado:
			print(f'{Cores.BOLD}{Cores.HEADER}ID \tDescricao \tIdCamping {Cores.ENDC}')
			for item in range(len(resultado)):
				print(f'{resultado[item][0]}  \t{resultado[item][1]}    \t{resultado[item][2]}')
		else:
			print(f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")
	elif tabela == 'acomodacao':
		c.execute("SELECT * FROM acomodacao INNER JOIN camping ON camping.id = idCamping;")
		resultado = c.fetchall()
		if resultado:
			print(f'{Cores.BOLD}{Cores.HEADER}ID \tNumero \tDescricao \tQtdPessoas \tIdCamping {Cores.ENDC}')
			for item in range(len(resultado)):
				print(f'{resultado[item][0]}  \t{resultado[item][1]}   \t{resultado[item][2]}   \t{resultado[item][3]}   \t{resultado[item][4]}')
		else:
			print(f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")
	elif tabela == 'preco':
		c.execute("SELECT * FROM preco INNER JOIN acomodacao ON acomodacao.id = idAcomodacao;")
		resultado = c.fetchall()
		if resultado:
			print(f'{Cores.BOLD}{Cores.HEADER}ID \tValor \tDescricao \tIdAcomodacao {Cores.ENDC}')
			for item in range(len(resultado)):
				print(f'{resultado[item][0]}  \t{resultado[item][1]}   \t{resultado[item][2]}   \t{resultado[item][3]}')
		else:
			print(f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")

	print(f"{Cores.BOLD}{Cores.OKGREEN}Pesquisa realizada com sucesso em {tabela}.{Cores.ENDC}")
	input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")

def pesquisarUnico(tabela, conn):

	c = conn.cursor()

	if tabela == 'camping':
		pesquisar(tabela, conn)
		x = int(input("Informe o id (camping) a pesquisar: "))
		c.execute("SELECT * FROM camping WHERE id = ?;", (x,))
		print(c.fetchall())
	elif tabela == 'endereco':
		pesquisar(tabela, conn)
		x = int(input("Informe o id (endereco) a pesquisar: "))
		c.execute("SELECT * FROM endereco WHERE id = ?;", (x,))
		print(c.fetchall())
	elif tabela == 'infraestrutura':
		pesquisar(tabela, conn)
		x = int(input("Informe o id (infraestrutura) a pesquisar: "))
		c.execute("SELECT * FROM infraestrutura WHERE id = ?;", (x,))
		print(c.fetchall())
	elif tabela == 'acomodacao':
		pesquisar(tabela, conn)
		x = int(input("Informe o id (acomodacao) a pesquisar: "))
		c.execute("SELECT * FROM acomodacao WHERE id = ?;", (x,))
		print(c.fetchall())
	elif tabela == 'preco':
		pesquisar(tabela, conn)
		x = int(input("Informe o id (preco) a pesquisar: "))
		c.execute("SELECT * FROM preco WHERE id = ?;", (x,))
		print(c.fetchall())

	print(f"{Cores.BOLD}{Cores.OKGREEN}Pesquisa realizada com sucesso em {tabela}.{Cores.ENDC}")
	input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")

def excluir(tabela, conn):

	c = conn.cursor()

	if tabela == 'camping':
		pesquisar(tabela, conn)
		x = input("Indique qual id a excluir: ")
		c.execute("DELETE FROM camping WHERE id=?", (x,))
		conn.commit()
	elif tabela == 'endereco':
		pesquisar(tabela, conn)
		x = input("Indique o id a excluir: ")
		c.execute("DELETE FROM endereco WHERE id=?", (x,))
		conn.commit()
	elif tabela == 'infraestrutura':
		pesquisar(tabela, conn)
		x = input("Indique o id a excluir: ")
		c.execute("DELETE FROM infraestrutura WHERE id=?", (x,))
		conn.commit()
	elif tabela == 'acomodacao':
		pesquisar(tabela, conn)
		x = input("Indique o id a excluir: ")
		c.execute("DELETE FROM acomodacao WHERE id=?", (x,))
		conn.commit()
	elif tabela == 'preco':
		pesquisar(tabela, conn)
		x = input("Indique o id a excluir: ")
		c.execute("DELETE FROM preco WHERE id=?", (x,))
		conn.commit()
		
	print(f"{Cores.BOLD}{Cores.OKGREEN}Exclusão com sucesso em {tabela}.{Cores.ENDC}")
	input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")