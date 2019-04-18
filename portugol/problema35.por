programa
{
	inclua biblioteca Texto --> txt
	
	funcao inicio()
	{
		cadeia palavra, inicial
		escreva("Bem vind@ ao sistema de verificação de palavras.\n")

		escreva("\nInforme uma palavra: ")
		leia(palavra)

		inicial = txt.extrair_subtexto(palavra, 0, 1)
		verificarInicial(inicial)
	}

	funcao verificarInicial(cadeia inicial) {
		se (inicial == "a" ou inicial == "e" ou inicial == "i" ou inicial == "o" ou inicial == "u") {
			escreva("A palavra começa por uma vogal.")
		} senao {
			escreva("A palavra NÃO começa por uma vogal.")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 290; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */