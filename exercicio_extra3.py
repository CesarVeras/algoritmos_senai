from math import sqrt
from utils import clear

def main():
    clear()
    print("Bem vindo ao sistema\n")
    numero1 = float(input("Informe um número: "))
    numero2 = float(input("Informe outro número: "))

    if (numero1 > numero2):
        numero1 = sqrt(numero1)
        numero2 = numero2 ** 2
        print("Primeiro número: %.1f\nSegundo número: %.1f" % (numero1, numero2))
    elif (numero1 < numero2):
        numero1 = numero1 ** 2
        numero2 = sqrt(numero2)
        print("Primeiro número: %.1f\nSegundo número: %.1f" % (numero1, numero2))
    else:
        print("Os números são iguais")


if __name__ == "__main__":
    main()