def main():
    totalPessoas = 10
    estados = estadosCivis = [""] * totalPessoas
    totalDeSC = totalDePR = totalDeRS = totalDeSolteiros = 0.0

    print("Bem vindo(a) ao algoritmo de Censo Demográfico.")
    for i in range(totalPessoas):
        estado = ""
        estadoCivil = ""
        valido = False

        while valido == False:
            valido = True
            entrada = input(
                'Digite o seu estado de origem e seu estado civil separados por ";"({} de {}): '.format(
                    (i + 1), totalPessoas
                )
            )

            estado = entrada[0:2]
            estadoCivil = entrada[3:4]

            if estado != "SC" and estado != "RS" and estado != "PR":
                print("O estado só pode ser do sul(SC, RS, PR).")
                valido = False

            if estadoCivil != "S" and estadoCivil != "C":
                print(
                    'O estado civil deve ser apenas "C" para casado(a) ou "S" para solteiro(a).'
                )
                valido = False

        estados[i] = estado
        estadosCivis[i] = estadoCivil
        if estadoCivil == "S":
            totalDeSolteiros += 1

        if estado == "SC":
            totalDeSC += 1
        elif estado == "RS":
            totalDeRS += 1
        else:
            totalDePR += 1

    porcentagemSC = (totalDeSC / totalPessoas) * 100
    porcentagemRS = (totalDeRS / totalPessoas) * 100
    porcentagemPR = (totalDePR / totalPessoas) * 100
    porcentagemSolteiros = (totalDeSolteiros / totalPessoas) * 100

    print(
        "Porcentagem de pessoas com origem no estado do Paraná: {}".format(
            porcentagemPR
        )
    )
    print(
        "Porcentagem de pessoas com origem no estado de Santa Cataria: {}".format(
            porcentagemSC
        )
    )
    print(
        "Porcentagem de pessoas com origem no estado do Rio Grande do Sul: {}".format(
            porcentagemRS
        )
    )
    print("Quantidade de pessoas solteiras: {}".format(totalDeSolteiros))
    print("Porcentagem de pessoas solteiras: {}".format(porcentagemSolteiros))


if __name__ == "__main__":
    main()
