def potencia(base, expoente):
	resultado = 1
	for i in range(expoente):
		resultado *= base
	return resultado

def main():
	base = 0
	expoente = 0
	print("Bem vind@ ao sistema de potência.")

	while (base < 2):
		base = int(input("Informe um número base MAIOR OU IGUAL a 2: "))

	while (expoente <= 1):
		expoente = int(input("Informe um número expoente MAIOR QUE 1: "))
	
	resultado = potencia(base, expoente)
	print("O número %i elevado a %i é %i" % (base, expoente, resultado))

if __name__ == "__main__":
	main()
