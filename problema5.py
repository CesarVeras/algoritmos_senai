def main():
    nome = input("Informe seu primeiro nome: ")
    sobrenome = input("Informe seu sobrenoem: ")
    idade = int(input("Informe sua idade: "))
    print("Olá %s %s, sua idade é de %i anos." % (nome, sobrenome, idade))


if __name__ == "__main__":
    main()
