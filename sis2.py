saldo_inicial = 10000


while True :
	print("----Banco----")
	print("1-Consultar Saldo")
	print("2-Lavantar dinheiro")
	print("3-Sair")
	escolhe = int(input("Escolhe Opção: "))
	
	if escolhe == 1:
		print("Saldo da Conta: ",saldo_inicial ,"kz" )
	elif escolhe == 2:
		print("Levantar Saldo")
		saldo = int(input("Quantia: "))	
		tent = 0
		while tent < 3:
			if saldo > saldo_inicial:
				print("Levantamento invalido" ,3 - tent)
				saldo = int(input("Levantar Novamente: " ))
				tent += 1
			if tent == 3:
				print("Lavantamento Bloqueado")
				saldo_inicial -= saldo
	elif escolhe == 3:
		print("Fim da operação")
		break

		"""
		Oque pude tirar de proveito nesse projeto:
		- melhor compreenção do while
		- melhor uso das condições
		- como repetir um codigo até for true

		"""

		


	