def main():
    maiorValor = None
    todosIguais = False

    print("Bem vindo ao sistema de verificação de valores.")

    valor1 = int(input("Informe o primeiro valor: "))
    valor2 = int(input("Informe o segundo valor: "))

    if (valor1 == valor2):
        todosIguais = True
    else:
        if (valor1 > valor2):
            maiorValor = valor1
        else:
            maiorValor = valor2
            
    if (todosIguais):
        print("Os valores são iguais")
    else:
        print("Maior valor é %i." % (maiorValor))

if __name__ == "__main__":
    main()