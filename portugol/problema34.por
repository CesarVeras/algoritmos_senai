programa
{
	
	funcao inicio()
	{
		inteiro numero
		logico primo
		escreva("Bem vind@ ao sistema de calculo de números primos.\n")

		escreva("\nInforme um número: ")
		leia(numero)
		escreva("Sequência de números primos entre 0 e " + numero)
		mostrarPrimos(numero)
	}

	funcao logico isPrimo(inteiro numero) {
		inteiro totalDivisores = 0
		para (inteiro i = 1; i <= numero; i++) {
			se (numero % i == 0) {
				totalDivisores++
			}
		}	

		retorne totalDivisores == 2
	}

	funcao mostrarPrimos(inteiro limite) {
		logico primo
		para (inteiro i = 0; i <= limite; i++) {
			primo = isPrimo(i)
			se (primo) {
				escreva("\n" + i)
			}
		}
	}
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 631; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */