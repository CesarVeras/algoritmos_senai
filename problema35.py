def verificarInicial(palavra):
	inicial = palavra[0].lower()
	if (inicial == 'a' or inicial == 'e' or inicial == 'i' or inicial == 'o' or inicial == 'u'):
		print('A palavra começa por uma vogal.')
	else:
		print('A palavra NÃO começa por uma vogal.')

def main():
	print("Bem vind@ ao sistema de verificação de palavras.")
	palavra = input("Informe uma palavra: ")
	verificarInicial(palavra)

if __name__ == "__main__":
	main()
