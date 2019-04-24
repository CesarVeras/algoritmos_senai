def main():
    numeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    saida = ""

    for i in range(0, len(numeros)):
        numeros[i] = int(input("Informe o nº %i: " % (i + 1)))

        if numeros[i] % 2 == 0:
            saida += "\nnº %i: %i é par." % ((i + 1), numeros[i])
        else:
            saida += "\nnº %i: %i é ímpar." % ((i + 1), numeros[i])
    print(saida)


if __name__ == "__main__":
    main()
