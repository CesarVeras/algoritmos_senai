programa
{
	
	funcao inicio()
	{
		// Criar uma algoritmo que leia o nome e a profissão de 6 pessoas.
		// Imprimir as profissões (sem repetição) e quantas pessoas têm cada uma das profissões listadas.
		const inteiro quantidade_pessoas = 6
		cadeia saida1 = "", saida2 = ""
		cadeia profissoes[] = {"", "", "", "", "", ""}, entradas[quantidade_pessoas]
		inteiro quantidade_profissoes[] = {0, 0, 0, 0, 0, 0}
		logico achou = falso
		
		escreva("Bem vindo(a) ao sistema.\n")

		para (inteiro i = 0; i < quantidade_pessoas; i++) {
			escreva("Informe o sua profissão (" + (i + 1) + "/" + quantidade_pessoas + "): ")
			leia(entradas[i])
		}
		para (inteiro i = 0; i < quantidade_pessoas; i++) {
			achou = falso
			para (inteiro j = 0; j < quantidade_pessoas; j++) {
				se (entradas[i] == profissoes[j]) {
					quantidade_profissoes[j]++
					achou = verdadeiro
					pare
				}
			}	
			se (nao achou) {
				para (inteiro j = 0; j < quantidade_pessoas; j++) {
					se (profissoes[j] == "") {
						profissoes[j] = entradas[i]
						quantidade_profissoes[j]++ 
						pare
					}
				}
			}
		}
		saida1 += "\nProfissões cadastradas:"
		saida2 += "\nQuantidade de funcionário das profissões:"
		para (inteiro i = 0; i < quantidade_pessoas; i++) {
			se (profissoes[i] != "") {
				saida1 += "\n" + profissoes[i]		
				saida2 += "\n" + profissoes[i] + ": " + quantidade_profissoes[i] + " pessoa(s)."
			}
		}
		escreva(saida1)
		escreva(saida2)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1076; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = {profissoes, 10, 9, 10}-{entradas, 10, 50, 8}-{quantidade_profissoes, 11, 10, 21};
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */