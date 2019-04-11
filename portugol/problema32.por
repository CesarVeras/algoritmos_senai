programa
{
	inclua biblioteca Matematica --> mat
	
	funcao inicio()
	{
		real graus, radianos
		escreva("Bem vind@ ao sistema de conversão de graus.\n")
		
		escreva("Informe o angulo em graus: ")
		leia(graus)

		radianos = calcularRadianos(graus)

		escreva(graus + " graus = " + radianos + " radianos")
	}

	funcao real calcularRadianos(real graus) {
		retorne mat.arredondar(((graus * mat.PI) / 180), 2)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 300; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */