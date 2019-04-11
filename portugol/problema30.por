programa
{
	inclua biblioteca Matematica --> mat	
	funcao inicio()
	{
		real raio, perimetro, area
		escreva("Bem vindo ao sistema de circunferências.\n")

		escreva("Informe o raio da circunferência: ")
		leia(raio)
		area = calculaArea(raio)
		perimetro = calculaPerimetro(raio)
		escreva("\nÁrea da circunferência: " + area)
		escreva("\nPerimetro da circunferência: " + perimetro)
	}


	funcao real calculaArea(real raio) {
		retorne mat.arredondar((mat.PI * mat.potencia(raio, 2.0)),2)
	}

	funcao real calculaPerimetro(real raio) {
		retorne mat.arredondar((2 * mat.PI * raio), 2)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 487; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */