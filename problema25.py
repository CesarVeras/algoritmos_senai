def main():
	soma = 0.0
	media = 0.0
	print("Bem vind@ ao sistema.\n")
	for i in range(1, 151):
		print(i)
		soma += i	
	media = soma / 150.0
	print("A soma dos número de 1 a 150 é %.2f" % soma)
	print("A média dos número de 1 a 150 é %.2f" % media)


if __name__ == "__main__":
	main()
