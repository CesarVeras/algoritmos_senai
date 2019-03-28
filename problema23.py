def main():
    print("Bem vindo ao sistema bancário.")
    nome = input("Informe o seu nome: ")
    rendaFamilia = float(input("Informe a sua renda familiar: R$"))

    if (rendaFamilia > 998):
        print("Desculpe %s, mas não podemos fornecer empréstimos para pessoas com renda familiar superior a um salário mínimo." % nome)
    else:
        valorEmprestimo = float(input("Informe o valor do empréstimo que deseja sacar: R$"))
        contador = 1
        divida = valorEmprestimo
        print("Empréstimo aprovado!")
        while (contador <= 10):
            divida -= valorEmprestimo * 0.1
            print("Saldo do mês nº%i: R$%.2f" % (contador, divida))
            contador += 1


if __name__ == "__main__":
    main()
