def main():
	print("Bem vind@ ao sistema de exibição de números multiplos de 5.")
	limiteInferior = int(input("Informe um limite inferior: "))
	# adiciona um pois o range no segundo argumento é um limite aberto
	limiteSuperior = int(input("Informe um limite superior: ")) + 1
	
	for i in range(limiteInferior, limiteSuperior):
		if (i % 5 == 0):
			print(i)

if __name__ == "__main__":
	main()
