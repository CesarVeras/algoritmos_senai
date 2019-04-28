def main():
	tamanho = 10
	valorProduto = valorVenda = [None] * tamanho
	lucroMenor10 = lucroEntre10e20 = lucroMaior20 = 0
	print("Bem vindo(a) ao sistema.")

	for i in range(0, tamanho):
		valorProduto[i] = float(input("Informe o valor do produto nº %i: " % (i + 1)))
		valorVenda[i] = float(input("Informe o valor da venda do produto nº %i: " % (i + 1)))

		lucro = (valorProduto[i] * valorVenda[i]) / 100 - 100
		if (lucro < 10):
			lucroMenor10 += 1
		elif (lucro >= 10 and lucro <= 20):
			lucroEntre10e20 += 1
		else:
			lucroMaior20 += 1

	print("Quantidade de Produtos com lucro menor do que 10%: {}\nQuantidade de Produtos com lucro entre 10% e 20%: {}\nQuantidade de Produtos com lucro maior que 20%: {}".format(lucroMenor10, lucroEntre10e20, lucroMaior20))
if __name__ == "__main__":
	main()
