def main():
    print("Bem vindo ao sistema de calculo de empréstimo.")

    salarioBruto = float(input("Informe o seu salário bruto: "))
    valorMaximoPrestacao = salarioBruto * 0.3

    valorPrestacao = float(input("Informe o valor da prestação que você deseja pagar: "))

    if (valorPrestacao > valorMaximoPrestacao):
        print("O empréstimo NÃO pode ser concedido.")
    else: 
        print("O empréstimo PODE ser concedido.")

if __name__ == "__main__":
    main()