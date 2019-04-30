programa
{
	
	funcao inicio()
	{
		const inteiro tamanho = 12
		real temperaturaMedia[tamanho], maiorTemperatura = 0.0, menorTemperatura = 0.0
		inteiro menorMes = 0, maiorMes = 0
		cadeia meses[] = {"janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", 
			"setembro", "outubro", "novembro", "dezembro"}
		
		escreva("Bem vindo(a) ao sistema.\n")
		
		para (inteiro i = 0; i < tamanho; i++) {
			escreva("Informe a temperatura média de " + meses[i] + " em Celsius: ")
			leia(temperaturaMedia[i])
			se (i == 0) {
				maiorTemperatura = temperaturaMedia[i]
				menorTemperatura = temperaturaMedia[i]
			}

			se (temperaturaMedia[i] < menorTemperatura) {
				menorTemperatura = temperaturaMedia[i]
				menorMes = i
			}

			se (temperaturaMedia[i] > maiorTemperatura) {
				maiorTemperatura = temperaturaMedia[i]
				maiorMes = i
			}
		}

		escreva("\nO mês com menor temperatura foi " + meses[menorMes] + " com " + menorTemperatura + "ºC.")
		escreva("\nO mês com maior temperatura foi " + meses[maiorMes] + " com " + maiorTemperatura + "ºC.")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 432; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */