def main():
	c1 = 1
	c2 = 1
	print("Bem vindo ao sistema")
	resposta = input("Deseja ver as tabuadas de 1 a 10(s/n)? ")
	if (resposta.lower() == 's'):
		while (c1 <= 10):
			c2 = 1
			while (c2 <= 10):
				multiplicacao = c1 * c2
				print('%i x %i = %i' % (c1, c2, multiplicacao))
				c2 += 1
			print('-----')
			c1 += 1
	else:
		print("Até mais!")

if __name__ == "__main__":
	main()
