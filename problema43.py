def main():
  tamanho = 3
  matriz = [[0] * tamanho] * tamanho
  saida = ''

  for i in range(tamanho):
    for j in range(tamanho):
      matriz[i][j] = int(input(f'Informe o elemento (linha {(i + 1)}, coluna {(j + 1)}): '))
      saida += f'{matriz[i][j]}'
      saida += '\t'
    saida += '\n'
  print(saida)

if __name__ == "__main__":
    main()