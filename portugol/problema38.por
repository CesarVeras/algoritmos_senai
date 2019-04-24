programa
{
	inclua biblioteca Util --> u
	
	funcao inicio()
	{
		cadeia saida = ""
		inteiro numeros[15]
		
		escreva("Bem vindo(a) ao sistema.\n")
		
		para(inteiro i = 0; i < u.numero_elementos(numeros); i++) {
			escreva("Informe o nº " + (i + 1) + ": ")
			leia(numeros[i])

			se (numeros[i] % 2 == 0) {
				saida += "\n" + (i + 1) + ": " + numeros[i] + " é par."
			} senao {
				saida += "\n" + (i + 1) + ": " + numeros[i] + " é ímpar."
			}
		}
		escreva(saida)	
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 475; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */