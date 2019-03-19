from math import exp

def main():
    contador = 0
    while contador < 10:
        valor = int(input("Informe o nº%i: " % (contador+1)))
        quadrado = valor**2
        print("Valor digitado %i e quadrado %i" % (valor, quadrado))
        contador += 1
if __name__ == "__main__":
    main()