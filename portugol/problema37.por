programa
{
	inclua biblioteca Util --> u
	
	funcao inicio()
	{
		cadeia nome[5], saida = "Aluno\tNota 1\tNota 2\tMédia"
		real nota1[5], nota2[5], media[5]
		
		escreva("Bem vindo(a) ao sistema.\n")
		
		
		para(inteiro i = 0; i < u.numero_elementos(nome); i++) {
			escreva("Informe o nome do(a) aluno(a) nº " + (i + 1) + ": ")
			leia(nome[i])
			
			escreva("Informe a nota nº 1 do(a) " + nome[i] + ": ")
			leia(nota1[i])

			escreva("Informe a nota nº 2 do(a) " + nome[i] + ": ")
			leia(nota2[i])

			media[i] = (nota1[i] + nota2[i]) / 2
			saida += "\n" + nome[i] + "\t" + nota1[i] + "\t" + nota2[i] + "\t" + media[i]
		}
		escreva(saida)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 430; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */