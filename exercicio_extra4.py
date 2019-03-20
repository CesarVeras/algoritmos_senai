from utils import clear

def main():
    numeros = []
    clear()
    print("Bem vindo ao sistema")
    for i in range(0,3):
        numeros.append(float(input("Informe o número %i: " % (i+1))))
    numeros.sort()
    print(numeros)

if __name__ == "__main__":
    main()