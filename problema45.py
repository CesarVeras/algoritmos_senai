import random

def main():
  linhas = 5
  colunas = 6
  limite_sorteios = 60
  sorteios = linhas * colunas
  matriz = [[0] * colunas] * linhas
  numeros_sorteados = [0] * sorteios
  aux = 0
  achou = False
  saida = "\nMatriz de números sorteados:\n"

  print('Bem vindo(a) ao sistema!')

  i = 0
  while (i < sorteios):
    achou = False
    aux = random.randint(1, limite_sorteios)
    if (i >= 1):
      j = 0
      while (j < (i - 1) and not achou):
        if (numeros_sorteados[j] == aux):
          achou = True
        else:
          j += 1

      if (not achou):
        numeros_sorteados[i] = aux
        i += 1

    else:
      numeros_sorteados[i] = aux
      i += 1

  print(numeros_sorteados)

  cont = 0
  for i in range(linhas):
    for j in range(colunas):
      matriz[i][j] = numeros_sorteados[cont]
      saida += '{}'.format(matriz[i][j]) + '\t'
      cont += 1
    saida += '\n'

  print(saida)

if __name__ == "__main__":
  main()