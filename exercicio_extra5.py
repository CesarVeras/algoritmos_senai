from utils import clear

def main():
    numeros = []
    clear()
    print("Bem vindo ao sistema")
    for i in range(0,3):
        numeros.append(float(input("Informe o número %i: " % (i+1))))
    numeros.sort()
    print("Menor valor: %.1f\nValor intermediário: %.1f\nMaior valor: %.1f" 
        % (numeros[0], numeros[1], numeros[2]))

if __name__ == "__main__":
    main()