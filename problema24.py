def main():
	soma = 0
	media = 0
	numero = 0	
	totalNumeros = -1
	primeiraVez = True
	print("Bem vind@ ao sistema de soma de número positivos.")
	while (primeiraVez or numero >= 0):
		primeiraVez = False
		soma += numero
		totalNumeros += 1
		numero = int(input("Informe um número positivo: "))
	if (totalNumeros == 0):
		media = 0.0
	else:
		media = soma / totalNumeros
	print("A soma dos números positivos é %i.\nA média dos números positivos foi de %.2f" % (soma, media))
if __name__ == "__main__":
	main()
