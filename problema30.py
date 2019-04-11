from math import pi

def calcularArea(raio):
	return pi * raio ** 2
	
def calcularPerimetro(raio):
	return 2 * pi * raio

def main():
	print("Bem vindo ao sistema de circunferências.")
	raio = float(input("Informe o raio da circunferência: "))
	area = calcularArea(raio)
	perimetro = calcularPerimetro(raio)
	print('Área: %.2f\nPerimetro: %.2f' % (area, perimetro))

if __name__ == "__main__":
	main()
