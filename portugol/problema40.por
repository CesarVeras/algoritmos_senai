programa
{
	
	funcao inicio()
	{
		const inteiro tamanho = 10
		inteiro iguais10 = 0, maioresMedia = 0, iguaisMedia = 0
		real numeros[tamanho], soma = 0.0, media
		escreva("Bem vindo(a) ao sistema.\n")

		para (inteiro i = 0; i < tamanho; i++) {
			escreva("Informe o um número real(" + (i + 1) + "/" + tamanho +"): ")
			leia(numeros[i])
			se (numeros[i] == 10) {
				iguais10++
			}
			soma += numeros[i]
		}

		media = soma / tamanho

		para (inteiro i = 0; i < tamanho; i++) {
			se (numeros[i] == media) {
				iguaisMedia++
			} senao se (numeros[i] > media) {
				maioresMedia++
			}
		}
		escreva("Média: " + media)
		escreva("\nQuantidade de números iguais a 10: " + iguais10
			+ "\nQuantidade de números maiores que a média: " + maioresMedia
			+ "\nQuantidade de números iguais a média: " + iguaisMedia)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 322; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */