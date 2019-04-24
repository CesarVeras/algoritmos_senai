def contaVogais(palavra):
    totalV = 0
    for i in range(0, len(palavra)):
        letra = palavra[i].lower()
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            totalV += 1
    return totalV


def main():
    print("Bem vindo(a) ao sistema de palavras.")
    palavra = input("Informe uma palavra: ")
    totalV = contaVogais(palavra)
    totalC = len(palavra) - totalV
    print("A palavra %s possui %i vogais e %i consoantes." % (palavra, totalV, totalC))


if __name__ == "__main__":
    main()
