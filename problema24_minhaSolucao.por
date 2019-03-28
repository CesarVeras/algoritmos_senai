programa
{
	
	funcao inicio()
	{
		real media = 0.0, numero = 0.0, soma = 0.0, totalNumeros = -1.0
		escreva("Bem vind@ ao sistema de soma de número positivos.\n")

		faca {
			totalNumeros++
			soma += numero
			
			escreva("Informe um número positivo: ")
			leia(numero)
		} enquanto (numero > 0)
		se (totalNumeros == 0) {
			media = 0.0
		} senao {
			media = soma / totalNumeros
		}
		escreva("\nA soma dos números positivos é " + soma + ".\nA média dos números positivos foi de " + media)
	}
}
