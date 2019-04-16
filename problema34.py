def isPrimo(numero):
    totalDivisores = 0
    for i in range(1, numero + 1):
        if (numero % i == 0):
            totalDivisores += 1
    return not (totalDivisores > 2)


def primosAteX(x):
    for i in range(0, x + 1):
        primo = isPrimo(i)
        if (primo):
            print(i)


def main():
    print('Bem vind@ ao sistema de calculo de números primos.')
    numero = int(input('Informe um número: '))
    print('Sequência de números primos entre 0 e %i:' % numero)
    primosAteX(numero)


if __name__ == "__main__":
    main()
