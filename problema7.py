def main():
    print("Bem vindo ao sistema de investimento")
    saldoInicial = float(input("Informe o valor que deseja depositar: "))
    quantidadeMeses = int(input("Informe a quantidade de meses que deseja aplicar: "))
    saldoFinal = saldoInicial + saldoInicial * 0.01 * quantidadeMeses
    print("Seu novo saldo é de %.2f" % saldoFinal)

if __name__ == "__main__":
    main()