def main():
	contador = 1
	soma = 0
	while(contador <= 100):
		if(contador % 2 == 0):
			soma += contador
			print(contador)
		contador+=1
	print('A soma dos pares de 1 a 100 é %i' % soma)

if __name__ == "__main__":
	main()