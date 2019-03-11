def main():
    print("Bem vindo ao sistema de avaliação de média")

    media = int(input("\nInforme sua média(0 a 100): "))

    if (media >= 0 and media <= 49):
        print("Média insuficiente.")
    elif (media >= 50 and media <= 64):
        print("Média regular.")
    elif (media >= 65 and media <= 84):
        print("Média boa.")
    elif (media >= 85 and media <= 100):
        print("Médiia ótima.")
    else:
        print("Nota inválida.")

if __name__ == "__main__":
    main()
