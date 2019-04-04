programa
{
	
	funcao inicio()
	{
		inteiro limiteSuperior, limiteInferior
	
		escreva("Bem vind@ ao sistema de exibição de números multiplos de 5.\n")

		escreva("Informe um limite inferior: ")
		leia(limiteInferior)

		escreva("Informe um limite superior: ")
		leia(limiteSuperior)

		para (inteiro i = limiteInferior; i <= limiteSuperior; i++) {
			se (i % 5 == 0) {
				escreva(i + "\n")
			}	
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 364; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */