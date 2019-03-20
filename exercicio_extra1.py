def main():
    print("Bem vindo ao sistema.")
    nome = input("Informe seu nome: ")
    sexo = input("Informe seu sexo: ")
    idade = int(input("Informe sua idade: "))

    if (sexo.lower() == "f" and idade < 25):
        print("%s aceita." % nome)
    else:
        print("%s não aceita." % nome)

if __name__ == "__main__":
    main()