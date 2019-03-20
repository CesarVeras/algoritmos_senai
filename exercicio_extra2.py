def main():
    print("Bem vindo ao sistema de estados.\n")
    estado = input("Informe a sigla de um estado: ")

    if (estado.upper() == "RJ"):
        print("Carioca")
    elif (estado.upper() == "SP"):
        print("Paulista")
    elif (estado.upper() == "MG"):
        print("Mineiro")
    else:
        print("Outros estados")

if __name__ == "__main__":
    main()