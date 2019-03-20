from utils import clear

def main():
    clear()
    print("Bem vindo ao sistema de calculo de lucro.")
    valor = float(input("Informe o valor do produto: "))

    if (valor < 20):
        lucro = valor * 0.45
    else:
        lucro = valor * 0.3
        
    valorVenda = valor + lucro
    print("O valor da venda foi de %.2f" % valorVenda)

if __name__ == "__main__":
    main()