def main():
	contador = 1
	soma = 0
	print("Bem vindo ao sistema!")
	limite = int(input("Informe o limite para os números: "))
	while (contador < limite):
		if (contador % 2 == 1):
			print(contador)
			soma += contador 
		contador += 1
	print('O resultado da soma dos números impares de 1 a %i foi de %i' % (limite, soma))

if __name__ == "__main__":
	main()
