import random

def main():
	nome = ["aaa", "aaa", "aaa", "aaa", "aaa"]
	nota1 = [0.0, 0.0, 0.0, 0.0, 0.0]
	nota2 = [0.0, 0.0, 0.0, 0.0, 0.0]
	media = [0.0, 0.0, 0.0, 0.0, 0.0]
	saida = "Aluno(a) Nota 1\tNota 2\tMédia"

	print("Bem vindo(a) ao sistema.")

	for i in range(0, len(nome)):
		nome[i] = input("Informe o nome do(a) aluno(a) nº %i: " % (i + 1))
		nota1[i] = float(input("Informe a nota nº 1 do(a) %s: " % (nome[i])))
		nota2[i] = float(input("Informe a nota nº 2 do(a) %s: " % (nome[i])))
		media[i] = (nota1[i] + nota2[i]) / 2
		saida += "\n{}\t {}\t{}\t{}".format(nome[i], nota1[i], nota2[i], media[i])
		
	print(saida)

if __name__ == "__main__":
	main()
