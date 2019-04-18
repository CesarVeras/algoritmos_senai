programa
{
	inclua biblioteca Texto --> txt
	
	funcao inicio()
	{
		cadeia palavra
		escreva("Bem vind@ ao sistema de palavras.\n")

		escreva("Informe uma palavra: ")
		leia(palavra)

		escreva("A palavra " + palavra + " possui " + totalVogais(palavra) + " vogais e " 
			+ totalConsoantes(palavra) + " consoantes.")
		
	}

	funcao inteiro totalVogais(cadeia palavra) {
		inteiro tamanhoPalavra = txt.numero_caracteres(palavra)
		inteiro quantidadeVogais = 0
		cadeia letra
		
		para (inteiro i = 0; i < tamanhoPalavra; i++) {
			letra = txt.extrair_subtexto(palavra, i, i + 1)
			se (letra == "a" ou letra == "e" ou letra == "i" ou letra == "o" ou letra == "u") {
				quantidadeVogais++
			}
		}
		retorne quantidadeVogais
	}

	funcao inteiro totalConsoantes(cadeia palavra) {
		inteiro tamanhoPalavra = txt.numero_caracteres(palavra)
		inteiro quantidadeConsoantes = 0
		cadeia letra
		
		para (inteiro i = 0; i < tamanhoPalavra; i++) {
			letra = txt.extrair_subtexto(palavra, i, i + 1)
			se (nao(letra == "a" ou letra == "e" ou letra == "i" ou letra == "o" ou letra == "u")) {
				quantidadeConsoantes++
			}
		}
		retorne quantidadeConsoantes
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1008; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */