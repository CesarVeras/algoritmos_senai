from utils import clear

def main():
    clear()
    print("Bem vindo ao sistema de calculo de conta.")
    nome = input("Informe o seu nome: ")
    conta = float(input("Informe o valor da conta: "))
    inicial = nome[0].lower()
    if (inicial == 'a' or inicial == 'd' or inicial == 'm' or inicial == 's'):
        valorFinal = conta * 0.7
        print("O valor que você precisa pagar é de %.2f" % valorFinal)
    else:
        print("Que pena. Nesta semana o desconto não é para seu nome, mas continue nos"             + " prestigiando que sua vez chegará")
        print("O valor que você precisa pagar é de %.2f" % conta)

if __name__ == "__main__":
    main()