def main():
	print("Bem vind@ ao sistema de calculo de temperatura.")
	limiteSuperior = int(input("Informe o limite superior das temperaturas em FAHRENHEIT: "))
	limiteInferior = int(input("Informe o limite inferior das temperaturas em FAHRENHEIT: "))
	decremento = int(input("Informe o intervalo de decremento das temperaturas: "))

	"""
	function range()
	param1: inicio, normalmente maior que o param2, fechado
	param2: fim, normalmente menor que o param2, aberto
	param3: step do laço, para ser um laço descrescente, 
		definir valor negativo e o param1 deve ser maior que o param2
	"""
	for i in range(limiteSuperior, limiteInferior - 1, -decremento):
		temperaturaC = (5 * (i - 32)) / 9
		print("%i Fahrenheit = %.2f Celsius" % (i, temperaturaC))

if __name__ == "__main__":
	main()
