quantidade_pessoas = 6
# entradas = [''] * quantidade_pessoas
entradas = ['Programador', 'Professor', 'Treinador', 'Lutador', 'Professor', 'Jornalista']
profissoes = [''] * quantidade_pessoas
quantidade_profissoes = [0] * quantidade_pessoas

def ler_dados():
  for i in range(quantidade_pessoas):
    entradas[i] = input('Informe a sua profissão({}/{}): '.format((i + 1), quantidade_pessoas))

def adicionar_nova_profissao(profissao):
  adicionou = False
  for i in range(quantidade_pessoas):
    if (profissoes[i] == '' and not adicionou):
      profissoes[i] = profissao
      quantidade_profissoes[i] += 1
      adicionou = True

def somar_profissao_existente(profissao):
  for i in range(quantidade_pessoas):
    if (profissao == profissoes[i]):
      quantidade_profissoes[i] += 1

def is_nova_profissao(profissao):
  for i in range(quantidade_pessoas):
    if (profissao == profissoes[i]):
      return False
  return True

def processar_dados():
  for i in range(quantidade_pessoas):
    if (is_nova_profissao(entradas[i])):
      adicionar_nova_profissao(entradas[i])
    else: 
      somar_profissao_existente(entradas[i])

def exibir_saida():
  saida1 = '\nProfissões cadastradas:'
  saida2 = '\nQuantidade de funcionários nas profissões:'
  for i in range(quantidade_pessoas):
    if (profissoes[i] != ''):
      saida1 += f"\n{profissoes[i]}"
      saida2 += f"\n{profissoes[i]}: {quantidade_profissoes[i]} pessoa(s)"
  print(saida1)
  print(saida2)

def main():
  print('Bem vindo(a) ao sistema!')

  # ler_dados()
  processar_dados()
  exibir_saida()

  
if __name__ == '__main__':
  main()