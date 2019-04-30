def main():
	tamanho = 10
	vetor = []
	saida = ""

	for i in range(tamanho):
		vetor.append(float(input("Informe um número ({}/{}): ".format(i, tamanho))))

	for i in range(int(tamanho / 2)):
		aux = vetor[i]
		vetor[i] = vetor[((tamanho - 1) - i)]
		vetor[((tamanho - 1) - i)] = aux

	for i in range(tamanho):
		saida += str(vetor[i])
		if i != tamanho - 1:
			saida += ", "
		else:
			saida += "."
	print(saida)

if __name__ == "__main__":
    main()
