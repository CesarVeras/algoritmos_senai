def main():
    achou = False
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    print("Bem vindo ao sistema de meses.")
    mes = int(input("Informe um número: "))

    for i in range(len(meses)):
        if (numeros[i] == mes):
            print(meses[i])
            achou = True
    
    if (not achou):
        print("Mês inexistente para o número informado.")
        
if __name__ == "__main__":
    main()