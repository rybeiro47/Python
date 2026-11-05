nome_aluno = input("Nome: ")
mat = float(input("Matematica: "))
tlp = float(input("TLP: "))
seac= float(input("SEAC: "))
tic = float(input("TIC: "))

notas =[]
notas.append(mat)
notas.append(tlp)
notas.append(seac)
notas.append(tic)
 
media = sum(notas)/4
maior = max(notas)
menor = min(notas)
quant_notas = len(notas)

positiva = 0
negativa = 0
for nota in notas:

	if nota >= 10:
		positiva += 1
	else:
		negativa += 1

	#saida

print("Nome do Estudante: ",nome_aluno)
print("Notas:" ,notas)
print("Média final: ",media)

print("Maior Nota: ",maior)
print("Menor Nota: ",menor)

print("Disciplinas Posetivas: ",positiva)
print("Disciplinas Negativas: ",negativa)


for no in notas:
	if no >= 0 and no <= 9:
		print ("Reprovado")
	elif no >= 10 and no <= 13:
		print ("Suficiente")
	elif no >= 14 and no <= 16:
		print ("Bom")
	elif no >= 17 and no <= 20:
		print ("Excelente")


"""
oque eu entendi nesse codigo?
*Aprendi alguns conceitos importantes de listas, 
como implementar uma condição em uma lista, como adicionar valores, como usar list + for + if
Aprendi um metodo para somar valores em estrutura de dados "Sum"
Aprendi com identificar o maior e menor numero em estrutura atrves de max e min
"""