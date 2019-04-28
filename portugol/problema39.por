programa
{
	inclua biblioteca Util
	
	funcao inicio()
	{
		const inteiro tamanho = 10
		real valorProduto[tamanho], valorVenda[tamanho], lucro
		inteiro precoMenor10 = 0, precoEntre10e20 = 0, precoMaior20 = 0
		escreva("Bem vindo(a) ao sistema.\n")

		para(inteiro i = 0; i < tamanho; i++){
			escreva("Informe o valor do produto nº" + (i + 1) + ": ")
			leia(valorProduto[i])

			escreva("Informe o valor da venda do produto º" + (i + 1) + ": ")
			leia(valorVenda[i])

			lucro = (valorProduto[i] * valorVenda[i]) / 100 - 100
			se (lucro < 10) {
				precoMenor10++
			} senao se (lucro >= 10 e lucro <= 20) {
				precoEntre10e20++
			} senao {
				precoMaior20++
			}
		}

		escreva("\nQuantidade de Produtos com lucro menor do que 10%: " + precoMenor10 
			 + "\nQuantidade de Produtos com lucro entre 10% e 20%: " + precoEntre10e20
			 + "\nQuantidade de Produtos com lucro maior que 20%:" + precoMaior20)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 404; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */