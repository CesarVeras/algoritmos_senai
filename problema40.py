def main():
    soma = 0
    iguais10 = 0
    iguaisMedia = 0
    maioresQueMedia = 0
    tamanho = 10
    numeros = []

    for i in range(0, tamanho):
        numeros.append(
            float(input("Informe um número real ({}/{}): ".format(i, tamanho)))
        )
        soma += numeros[i]

    media = soma / tamanho

    for i in range(0, tamanho):
        if numeros[i] == 10:
            iguais10 += 1
        if numeros[i] == media:
            iguaisMedia += 1
        elif numeros[i] > media:
            maioresQueMedia += 1

    print("Média: {}".format(media))
    print(
        "Quantidade de números iguais a 10: {}".format(iguais10)
        + "\nQuantidade de números maiores que a média: {}".format(maioresQueMedia)
        + "\nQuantidade de números iguais a média: {}".format(iguaisMedia)
    )


if __name__ == "__main__":
    main()
