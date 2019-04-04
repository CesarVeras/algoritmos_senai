programa
{
	inclua biblioteca Matematica --> mat
	
	funcao inicio()
	{
		inteiro limiteSuperior, limiteInferior, decremento 
		real temperaturaC = 0.0
		
		escreva("Bem vind@ ao sistema de calculo de temperatura.\n")
		
		escreva("Informe o limite superior de temperatura em FAHRENHEIT: ")
		leia(limiteSuperior)
		
		escreva("Informe o limite inferior de temperatura em FAHRENHEIT: ")
		leia(limiteInferior)

		escreva("Informe o intervalo de decremento das temperaturas: ")
		leia(decremento)

		para (inteiro i = limiteSuperior; i >= limiteInferior; i-=decremento) {	
			temperaturaC = (5.0 * (i - 32.0)) / 9.0
			temperaturaC = mat.arredondar(temperaturaC, 2)
			escreva(i + " Fahrenheit = " + temperaturaC + " Celsius\n")
		}
			
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 114; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */