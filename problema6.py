def main():
    print("Bem vindo ao sistema de calculo de médias.")
    nota1 = float(input("Informe a notaº 1: "))
    nota2 = float(input("Informe a notaº 2: "))
    nota3 = float(input("Informe a notaº 3: "))
    nota4 = float(input("Informe a notaº 4: "))

    media = (nota1 + (nota2 * 2) + (nota3 * 3) + (nota4 * 4)) / 10
    print("Sua média foi de %.1f" % media)

if __name__ == "__main__":
    main()