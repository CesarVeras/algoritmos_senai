programa
{
	inclua biblioteca Matematica --> mtm
	inclua biblioteca Tipos --> tp
	inclua biblioteca Texto --> txt
	
	funcao inicio()
	{
		cadeia byte
		inteiro numeroDecimal
		
		escreva("Bem vindo(a) ao sistema de conversão de binários para decimal.\n")
		
		escreva("\nInforme um byte: ")
		leia(byte)

		numeroDecimal = traduzirByte(byte)
		se (numeroDecimal != -1)
			escreva("O byte " + byte + " em decimal é " + numeroDecimal)
	}

	funcao inteiro traduzirByte(cadeia byte) {
		se (verificarByteValido(byte)) {
			inteiro soma = 0
			inteiro tamanho = txt.numero_caracteres(byte)
			inteiro digito
			inteiro expoente = 0
			para (inteiro i = tamanho - 1; i >= 0; i--) {
				digito = tp.cadeia_para_inteiro(txt.extrair_subtexto(byte, i, i + 1), 10)
				soma += digito * mtm.potencia(2, expoente)
				expoente++
			}
			retorne soma
		} senao {
			escreva("\nO valor digitado é inválido. O número deve conter apenas 0 ou 1 e ter no máximo 8 digitos.")
			retorne -1
		}
	}

	funcao logico verificarByteValido(cadeia byte) {
		inteiro tamanho = txt.numero_caracteres(byte)
		se (tamanho > 8) {
			retorne falso
		}
		cadeia digito
		para (inteiro i = 0; i < tamanho; i++) {
			digito = txt.extrair_subtexto(byte, i, i + 1)
			se (digito != "0" e digito != "1") {
				retorne falso
			}
		}
		retorne verdadeiro
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 341; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */