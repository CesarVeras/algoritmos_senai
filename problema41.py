from utils import meses

def main():
    tamanho = 12
    menorMes = 0
    maiorMes = 0
    menorTemperatura = 0.0
    maiorTemperatura = 0.0
    temperaturas = []

    for i in range(tamanho):
        temperaturas.append(
            float(input("Informe a temperatura média de {}: ".format(meses[i])))
        )
        if i == 0:
            menorTemperatura = temperaturas[i]
            maiorTemperatura = temperaturas[i]

        if temperaturas[i] < menorTemperatura:
            menorTemperatura = temperaturas[i]
            menorMes = i

        if temperaturas[i] > maiorTemperatura:
            maiorTemperatura = temperaturas[i]
            maiorMes = i

    print(
        "O mês com a menor temporatura foi {} com {}ºC.".format(
            meses[menorMes], menorTemperatura
        )
    )
    print(
        "O mês com a maior temporatura foi {} com {}ºC.".format(
            meses[maiorMes], maiorTemperatura
        )
    )


if __name__ == "__main__":
    main()
