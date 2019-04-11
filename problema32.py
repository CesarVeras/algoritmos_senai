from math import pi

def calcularRadianos(graus):
	return (graus * pi) / 180


def main():
	print("Bem vind@ ao sistema de conversão de graus.")

	graus = float(input("Informe o angulo em graus: "))

	radianos = calcularRadianos(graus)

	print("%.2f graus = %.2f radianos" % (graus, radianos))


if __name__ == "__main__":
	main()
