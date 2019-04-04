def main():
	print("Bem vind@ ao sistema de visualização de tabuada.")
	resposta = input("Deseja visualizar a tabuada de 1 a 10 (S/N): ")

	if (resposta.lower() == 's'):
		for i in range(1, 11):
			for j in range(1, 11):
				resultado = i * j
				print("%i x %i = %i" % (i, j, resultado))
			print("")

if __name__ == "__main__":
	main()
