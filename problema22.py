def fatorial(numero):
    if (numero == 1):
        return 1
    else:
        return (numero * fatorial(numero - 1))


def main():
    print('Bem vindo ao sistema!')
    entrada = int(input('Digite um número para o cálculo do fatorial: '))
    contador = entrada
    saida = 'Resposta: %i! = %i' % (entrada, entrada)

    while (contador > 1):
        contador -= 1
        saida += ' x  %i' % contador
    print(saida + ' = %i' % fatorial(entrada))


if __name__ == "__main__":
    main()
