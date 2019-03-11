def main():
    maiorValor = None
    menorValor = None
    todosIguais = False

    print("Bem vindo ao sistema de verificação de valores.")

    valor1 = int(input("Informe o primeiro valor: "))
    valor2 = int(input("Informe o segundo valor: "))
    valor3 = int(input("Informe o terceiro valor: "))

    if (valor1 == valor2 and valor1 == valor3):
        todosIguais = True
    else:
        if (valor1 > valor2 and valor1 > valor3):
            maiorValor = valor1
        elif (valor2 > valor1 and valor2 > valor3):
            maiorValor = valor2
        elif (valor3 > valor1 and valor3 > valor2):
            maiorValor = valor3
        elif (valor1 == valor2 or valor1 == valor3):
            maiorValor = valor1
        else:
            maiorValor = valor2

        if (valor1 < valor2 and valor1 < valor3):
            menorValor = valor1
        elif (valor2 < valor1 and valor2 < valor3):
            menorValor = valor2
        elif (valor3 < valor1 and valor3 < valor2):
            menorValor = valor3
        elif (valor1 == valor2 or valor1 == valor3):
            menorValor = valor1
        else:
            menorValor = valor2

    if (todosIguais):
        print("Todos os valores são iguais")
    else:
        print("Maior valor é %i e o menor valor é %i" % (maiorValor, menorValor))

if __name__ == "__main__":
    main()