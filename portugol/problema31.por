programa
{
	
	funcao inicio()
	{
		real distancia, minutos, velocidadeMedia
		escreva("Bem vind@ ao sistema de calculo de velocidade média.\n")
		
		escreva("Informe a distância da viagem (em km): ")
		leia(distancia)

		escreva("Informe o tempo da viagem (em minutos): ")
		leia(minutos)

		velocidadeMedia = calcularVelocidadeMedia(distancia, minutos)
		escreva("A sua velocidade média foi de " + velocidadeMedia + " km/h.")
	}

	funcao real calcularVelocidadeMedia(real distancia, real minutos) {
		real horas = minutos / 60
		retorne distancia / horas
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 425; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */