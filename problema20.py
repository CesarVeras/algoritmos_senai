def main():
	contador = 1
	numero = int(input("Informe um número de 1 a 10 para consultar sua tabuada: "))

	if (numero > 0 and numero <= 10):
		while(contador <= 10):
			print("%i x %i = %i" % (numero, contador, (numero*contador)))
			contador += 1
	else:
		print("Tabuada inválida.")

if __name__ == "__main__":
	main()
