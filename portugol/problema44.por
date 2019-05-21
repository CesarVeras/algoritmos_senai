programa
{
	
	funcao inicio()
	{
		const inteiro tamanho = 3
		real matriz_a[tamanho][tamanho]
		real matriz_b[tamanho][tamanho]
		real soma[tamanho][tamanho]
		real media[tamanho][tamanho]
		cadeia saida_soma = "\nMatriz SOMA: \n"
		cadeia saida_media = "\nMatriz MÉDIA: \n"
		
		escreva("Bem vindo(a) ao sistema.\n")

		// Ler matriz A
		escreva("Leitura da matriz A:\n")
		para(inteiro i = 0; i < tamanho; i++){
			para(inteiro j = 0; j < tamanho; j++) {
				escreva("Informe o elemento(l: " + (i + 1) + ", c: " + (j + 1) + "): ")
				leia(matriz_a[i][j])
			}
		}

		// Ler matriz B
		escreva("Leitura da matriz B:\n")
		para(inteiro i = 0; i < tamanho; i++){
			para(inteiro j = 0; j < tamanho; j++) {
				escreva("Informe o elemento(l: " + (i + 1) + ", c: " + (j + 1) + "): ")
				leia(matriz_b[i][j])
				soma[i][j] = matriz_a[i][j] + matriz_b[i][j]
				saida_soma += soma[i][j] + "\t"
				media[i][j] = soma[i][j] / 2 
				saida_media += media[i][j] + "\t"
			}
			saida_soma += "\n"
			saida_media += "\n"
		}
		escreva(saida_soma)
		escreva(saida_media)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1069; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */