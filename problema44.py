#coding: utf-8

def main():
  tamanho = 3
  matriz_a = [[1.0] * tamanho] * tamanho
  matriz_b = [[3.0] * tamanho] * tamanho
  soma = [[0.0] * tamanho] * tamanho
  media = [[0.0] * tamanho] * tamanho
  saida_soma = '\nMatriz SOMA:\n'
  saida_media = '\nMatriz MÉDIA:\n'

  print('Bem vindo(a) ao sistema!')
  print('\nLeitura da matriz A:')
  for i in range(tamanho):
    for j in range(tamanho):
      matriz_a[i][j] = float(input(f'Informe o elemento(l:{(i + 1)}, c:{(j + 1)}): '))
      
  print('\nLeitura da matriz B:')
  for i in range(tamanho):
    for j in range(tamanho):
      matriz_b[i][j] = float(input(f'Informe o elemento(l:{(i + 1)}, c:{(j + 1)}): '))
      soma[i][j] = matriz_a[i][j] + matriz_b[i][j]
      saida_soma += ('{}'.format(soma[i][j]) + '\t')
      media[i][j] = soma[i][j] / 2
      saida_media += ('{}'.format(media[i][j])  + '\t')
    saida_soma += '\n'
    saida_media += '\n'

  print(saida_soma)
  print(saida_media)

if __name__ == "__main__":
    main()