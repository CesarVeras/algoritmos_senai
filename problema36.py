def contaVogais(palavra):
	totalV = 0
	for i in range(0, len(palavra)):
		letra = palavra[i].lower()
		if (letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
			totalV += 1
	return totalV

def contaConsoantes(palavra):
	totalC = 0
	for i in range(0, len(palavra)):
		letra = palavra[i].lower()
		if (not(letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u')):
			totalC += 1
	return totalC

def main():
	print("Bem vind@ ao sistema de palavras.")
	palavra = input("Informe uma palavra: ")
	totalV = contaVogais(palavra)
	totalC = contaConsoantes(palavra)
	print('A palavra %s possui %i vogais e %i consoantes.' % (palavra, totalV, totalC))

if __name__ == "__main__":
	main()
