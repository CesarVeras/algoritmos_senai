from utils import clear

def main():
    clear()
    print("Bem vindo ao sistema de calculo de verificar data.")
    dia = int(input("Informe o dia: "))
    mes = int(input("Informe o mês: "))
    ano = int(input("Informe o ano: "))

    if (ano >= 0):
        if (mes > 0 and mes <= 12):
            if (mes == 2):
                if (dia > 0 and dia <= 29):
                    print("Data válida.")
                else:
                    print("Data inválida.")
            elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
                if (dia > 0 and dia <= 30):
                    print("Data válida.")
                else:
                    print("Data inválida.")
            else:
                if (dia > 0 and dia <= 31): 
                    print("Data válida.")
                else:
                    print("Data inválida.")
        else:
            print("Data inválida.")
    else:
        print("Data inválida.")

if __name__ == "__main__":
    main()