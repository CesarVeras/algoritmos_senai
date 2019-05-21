programa
{
	inclua biblioteca Util --> u
	funcao inicio()
	{
		inteiro matriz[5][6]
		inteiro numerosSorteados[30]
		inteiro aux
		logico achou = falso
		cadeia saida = "\nMatriz de número sorteados:\n"
		
		escreva("Bem vindo(a) ao sistema!\n")

		inteiro i = 0
		enquanto(i < 30) {
			achou = falso
			aux = u.sorteia(1, 60)
			se (i >= 1) {
				inteiro j = 0
				enquanto (j < (i - 1) e nao achou) {
					se (numerosSorteados[j] == aux) {
						achou = verdadeiro
					} senao {
						j++
					}
				}
				se (nao achou) {
					numerosSorteados[i] = aux
					i++
				}
			} senao {
				numerosSorteados[i] = aux
				i++
			}
		}

		inteiro cont = 0
		para(i = 0; i < 5; i++) {
			para(inteiro j = 0; j < 6; j++) {
				matriz[i][j] = numerosSorteados[cont]
				saida += matriz[i][j] + "\t"
				cont++
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
 * @POSICAO-CURSOR = 625; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = {numerosSorteados, 7, 10, 16};
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */