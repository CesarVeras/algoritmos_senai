from math import pi

def main():
    print("Bem vindo ao sistema de calculo de diâmetro e comprimento de circunferência.")
    raio = float(input("Informe o valor do raio: "))
    diametro = raio * 2
    comprimento = diametro * pi
    print("O valor do diâmetro é de %.2f\nO valor do comprimento da circunferência é de %.2f" % (
        diametro, comprimento))

if __name__ == "__main__":
    main()
