def main():
    print("Bem vindo ao sistema de calculo de consumo de gasolina.")
    tipo = input("Informe o tipo do seu carro: ")
    percurso = float(input("Informe o percurso em quilômetros: "))

    if (tipo.lower() == 'a'):
        consumo = percurso / 12
        print("Seu consumo foi de %.2f litro(s)" % (consumo))
    elif (tipo.lower() == 'b'): 
        consumo = percurso / 9
        print("Seu consumo foi de %.2f litro(s)" % (consumo))
    elif (tipo.lower() == 'c'):
        consumo = percurso / 8
        print("Seu consumo foi de %.2f litro(s)" % (consumo))
    else:
        print("Tipo de carro inválido!")
        
if __name__ == "__main__":
    main()