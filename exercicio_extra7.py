from utils import clear

def main():
    clear()
    sala1 = 'abcdefghijk'
    sala2 = 'lmn'
    print("Bem vindo ao sistema de calculo de ensalamento.")
    nome = input("Informe o seu nome: ")
    inicial = nome[0].lower()
    if (sala1.find(inicial) != -1):
        print("Sala 101")
    elif (sala2.find(inicial) != -1):
        print('Sala 102')
    else:
        print('Sala 103')

if __name__ == "__main__":
    main()