programa
{
	
	funcao inicio()
	{
		const inteiro tamanho = 3
		inteiro matriz[tamanho][tamanho]
		cadeia saida = ""
		para (inteiro i = 0; i < tamanho; i++) {
			para (inteiro j = 0; j < tamanho; j++) {
				escreva("Informe o elemento(l:" + (i + 1) + ", c:" + (j + 1) + "): ")
				leia(matriz[i][j])
				saida += matriz[i][j]
				saida += "\t"
			}
			saida += "\n"
		}
		escreva(saida)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 122; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */