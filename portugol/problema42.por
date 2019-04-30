programa
{
	
	funcao inicio()
	{
		const inteiro tamanho = 10
		real vetor[tamanho], auxiliar

		escreva("Bem vindo(a) ao sistema.\n")

		para (inteiro i = 0; i < tamanho; i++) {
			escreva("Informe um número(" + (i + 1) + "/" + tamanho + "): ")
			leia(vetor[i])	
		}

		para(inteiro i = 0; i < tamanho/2; i++) {
			auxiliar = vetor[i]
			vetor[i] = vetor[(tamanho - 1) - i]
			vetor[tamanho - 1 - i] = auxiliar
		}

		para(inteiro i = 0; i < tamanho; i++) {
			escreva(vetor[i])
			se (i != (tamanho - 1)) {
				escreva(", ")
			} senao {
				escreva(".")
			}
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 485; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = {vetor, 7, 7, 5}-{auxiliar, 7, 23, 8};
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */