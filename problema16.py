def main():
    classeA = "R$ 11.262,00 ou mais."
    classeB = "R$ 8.641,00 a R$ 11.261,00."
    classeC = "R$ 2.005,00 a R$ 8.640,00."
    classeD = "R$ 1.255,00 a R$ 2.004,00."
    classeE = "R% 0,00     a R$ 1.254,00."

    classe = input("Informe sua classe social: ")

    if (classe.upper() == 'A'):
        print("Seu salário é de %s" % classeA)
    elif (classe.upper() == 'B'):
        print("Seu salário é de " + classeB)
    elif (classe.upper() == 'C'):
        print("Seu salário é de " + classeC)
    elif (classe.upper() == 'D'):
        print("Seu salário é de " + classeD)
    elif (classe.upper() == 'E'):
        print("Seu salário é de " + classeE)
    else:
        print

if __name__ == "__main__":
    main()