programa
{
	
	funcao inicio()
	{
		caracter resposta
		inteiro resultado
		
		escreva("Bem vind@ ao sistema de visualização de tabuada.")
		
		escreva("Deseja visualizar a tabuada de 1 a 10 (S/N): ")
		leia(resposta)

		se (resposta == 's' ou resposta == 'S') {
			para (inteiro i = 1; i <= 10; i++) {
				para (inteiro j = 1; j <=10; j++) {
					resultado = i * j
					escreva(i +  " x " + j + " = " + resultado + "\n")
				}
				escreva("\n")
			}
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 223; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */