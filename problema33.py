def isPrimo(numero):
    totalDivisores = 0
    for i in range(1, numero + 1):
        if (numero % i == 0):
            totalDivisores += 1
    return not (totalDivisores > 2)


def primosDeXaY(x, y):
    for i in range(x, y + 1):
        primo = isPrimo(i)
        if (primo):
            print('%i é primo' % i)


def main():
    print('Bem vind@ ao sistema de calculo de números primos.')
    numero = int(input('Informe um número: '))
    primo = isPrimo(numero)
    if (primo):
        print('%i é primo.' % numero)
    else:
        print('%i não é primo.' % numero)


if __name__ == "__main__":
    main()
    # primosDeXaY(1, 1000)
