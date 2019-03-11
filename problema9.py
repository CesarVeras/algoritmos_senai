def main():
    media = 0
    
    print("Bem vindo ao sistema de aprovação de alunos.")
    media = float(input("Informe sua média: "))

    if (media >= 7):
        print("APROVADO!")
    elif (media < 5):
        print("REPROVADO!")
    else:
        print("RECUPERAÇÃO!")


if __name__ == "__main__":
    main()