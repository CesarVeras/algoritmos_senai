import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def criarArquivoAlgoritmos():
    tipo = int(input("Informe que tipo de arquivo deseja criar:\n\t1 - problema\n\t2 - extra\n"))
    numero = int(input("Informe o número do arquivo:\n"))

    if (tipo == 1):
        nome = ('problema%i.py' % numero)
    else:
        nome = ('exercicio_extra%i.py' % numero)
    
    arquivo = open(nome, "x")
    arquivo.write('def main():\n')
    arquivo.write('\t\n')
    arquivo.write('\n')
    arquivo.write('if __name__ == "__main__":\n')
    arquivo.write('\tmain()\n')
    arquivo.close()

if __name__ == "__main__":
    escolha = int(input("Informe o que deseja fazer:\n\t1 - Criar Arquivo de Algoritmos\n"))
    if (escolha == 1):
        criarArquivoAlgoritmos()