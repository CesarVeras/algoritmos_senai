import os

meses = [
    "janeiro",
    "fevereiro",
    "março",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro",
]


def clear():
    os.system("cls" if os.name == "nt" else "clear")


"""
    Função responsável por criar um arquivo python, baseado nas respostas adquiridas pelo usuário.
    
    Se o usuário disser que quer criar um problema, o sistema irá perguntar que número dar ao nome do arquivo, criará um arquivo com o nome problemaX, sendo X o número passado pelo usuário.

    Se o usuário disser que quer criar um extra, o sistema irá perguntar que número dar ao nome do arquivo, criará um arquivo com o nome exercicio_extraX, sendo X o número passado pelo usuário.
"""


def criarArquivoAlgoritmos():
    tipo = int(
        input(
            "Informe que tipo de arquivo deseja criar:\n\t1 - problema\n\t2 - extra\n"
        )
    )
    numero = int(input("Informe o número do arquivo:\n"))

    if tipo == 1:
        nome = "problema%i.py" % numero
    else:
        nome = "exercicio_extra%i.py" % numero

    arquivo = open(nome, "x")
    arquivo.write("def main():\n")
    arquivo.write("\t\n")
    arquivo.write("\n")
    arquivo.write('if __name__ == "__main__":\n')
    arquivo.write("\tmain()\n")
    arquivo.close()


if __name__ == "__main__":
    escolha = int(
        input("Informe o que deseja fazer:\n\t1 - Criar Arquivo de Algoritmos\n")
    )
    if escolha == 1:
        criarArquivoAlgoritmos()
