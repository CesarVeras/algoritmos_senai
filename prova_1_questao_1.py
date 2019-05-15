def calcularRelacao(precoEtanol, precoGasolina):
    relacao = precoEtanol / precoGasolina
    if relacao <= 0.73:
        print("Para os preços informados, a melhor opção é a utilização da ETANOL")
    else:
        print("Para os preços informados, a melhor opção é a utilização da GASOLINA")


def main():
    continuar = "s"
    while continuar == "s" or continuar == "S":
        precoGasolina = 0.0
        precoEtanol = 0.0
        print("Bem vindo(a) a Calculadora Gasolina/Etanol.")
        while precoGasolina < 0.01 or precoGasolina > 10:
            precoGasolina = float(input("Digite o preço da Gasolina em R$: "))
            if precoGasolina < 0.01 or precoGasolina > 10:
                print("\nPreço inválido")

        while precoEtanol < 0.01 or precoEtanol > 10:
            precoEtanol = float(input("Digite o preço do Etanol em R$: "))
            if precoEtanol < 0.01 or precoEtanol > 10:
                print("\nPreço inválido")

        calcularRelacao(precoEtanol, precoGasolina)

        continuar = input("Deseja continuar(S/n): ")


if __name__ == "__main__":
    main()
