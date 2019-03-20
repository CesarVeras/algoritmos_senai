from utils import clear

def main():
    clear()
    print("Bem vindo ao sistema de calculo de peso ideal.")
    sexo = input("Informe o seu sexo(M/F): ")
    altura = float(input("Informe sua altura: "))

    if (sexo.lower() == "m"):
        pesoIdeal = (72.7 * altura) - 58
    else: 
        pesoIdeal = (62.1 * altura) - 44.7

    print("Seu peso ideal é de %.2fkg" % pesoIdeal)

if __name__ == "__main__":
    main()