def calcularVelocidade(distancia, minutos):
	horas = minutos / 60
	return distancia / horas

def main():
	print("Bem vind@ ao sistema de calculo de velocidade média.")
	
	distancia = float(input("Informe a distância da viagem (em km): "))
	minutos = float(input("Informe o tempo da viagem (em minutos): "))

	velocidadeMedia = calcularVelocidade(distancia, minutos)

	print("A sua velocidade média foi de %.2f km/h." % velocidadeMedia)

if __name__ == "__main__":
	main()
