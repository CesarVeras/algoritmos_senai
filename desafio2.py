def verificarByteValido(byte):
	tamanho = len(byte)
	if (tamanho > 8):
		return False

	for i in range(len(byte)):
		if (byte[i] != '1' and byte[i] != '0'):
			return False
    
	return True

def traduzirByte(byte):
	if (verificarByteValido(byte)):
		soma = 0
		expoente = 0	
		for i in range(len(byte)-1, -1, -1):
			soma += 2**expoente * int(byte[i])
			expoente += 1
		return soma
	else:
		print("O valor digitado é inválido. O número deve conter apenas 0 ou 1 e ter no máximo 8 digitos.")
		return -1

def main():
	print("Bem vindo(a) ao sistema de conversão de binário para decimal.")
	byte = input("Informe um byte: ")

	numeroDecimal = traduzirByte(byte)

	if (numeroDecimal != -1):
		print("O byte %s em decimal é %i" % (byte,numeroDecimal))
	
if __name__ == '__main__':
    main()