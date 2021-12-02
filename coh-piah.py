##Chama módulo de Expressões regulares
import re


##Função para ler a assinatura
def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''

    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

'''============================================================================================================================================================'''

##Função para ler os textos
def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos
'''============================================================================================================================================================'''

##Função separa sentenças
def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas
'''============================================================================================================================================================'''

##Função separa frases
def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)
'''============================================================================================================================================================'''


##Função separa palavras
def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()
'''============================================================================================================================================================'''


##Função numero de palavras
def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas
'''============================================================================================================================================================'''


##Função palavras diferentes
def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

'''============================================================================================================================================================'''



def compara_assinatura(as_a, as_b):
     '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
     S = 0
     for i in range (0, 6): #i vai de 0 a 5 = 6 traços linguísticos
         S = S + (abs(as_a[i] - as_b[i]))
     grau = S/6
     if grau < 0:
         grau = grau * (-1)
     return grau

    ##pass

'''============================================================================================================================================================'''

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)

    lista_frases = []
    for s in sentencas:
        frases_separadas = separa_frases(s)
        # separa_frases retorna um item de lista para cada sentença
        # e esses itens são unidos em uma única lista, frases
        for frases in frases_separadas:
            lista_frases.append(frases)

    lista_palavras = []
    for f in lista_frases:
        palavras_separadas = separa_palavras(f)
        for palavras in palavras_separadas:
            lista_palavras.append(palavras)
    assinatura = []

    assinatura.append(tamanho_medio_palavras(lista_palavras))
    assinatura.append(relacao_type_token(lista_palavras))
    assinatura.append(razao_hapax_legomana(lista_palavras))
    assinatura.append(tamanho_medio_de_sentenca(sentencas))
    assinatura.append(complexidade_de_sentenca(lista_frases, sentencas))
    assinatura.append(tamanho_medio_de_frase(lista_frases))

    return assinatura
    
    ##pass





'''============================================================================================================================================================'''
def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n)
    do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    i = 0
    assinatura_texto = calcula_assinatura(textos[i]) #calcula a assinatura do primeiro texto
    grau_similaridade = compara_assinatura(assinatura_texto, ass_cp) #verifica o grau de similaridade do primeiro texto com a assinatura do aluno
                                                                            #infectado com COH-PIAH
    
    menor_grau = grau_similaridade  #este será definido como o menor grau de similaridade (quanto mais similares eles forem, menor será o grau)
    texto_infectado = i + 1   #o texto 0 será definido como o texto infectado, inicialmente
    i = i+1

    while i <(len (textos)): #depois e preciso fazer o mesmo com o restante dos textos
        assinatura_texto = calcula_assinatura(textos[i])
        grau_similaridade = compara_assinatura(assinatura_texto, ass_cp) #cp = coh-piah
        if grau_similaridade < menor_grau:  #se o texto sendo analisado tem o grau menor do que o armazenado, 
            menor_grau = grau_similaridade  #substitui o valor
            texto_infectado = i + 1             #e também o índice do texto infectado
        i = i+1

    print ("O autor do texto %d está infectado com COH-PIAH" %(texto_infectado))
    return texto_infectado

    
    ##pass

'''============================================================================================================================================================'''        


'''============================================================================================================================================================'''        


    
# Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras:
def tamanho_medio_palavras(palavras):
    tamanho_das_palavras = 0
    total_de_palavras = len(palavras)
    for palavra in palavras:
        tamanho_das_palavras = tamanho_das_palavras + len(palavra)

    return tamanho_das_palavras/total_de_palavras
'''============================================================================================================================================================'''        
 



# Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras.
def relacao_type_token(palavras):
    return n_palavras_diferentes(palavras) / len(palavras)

'''============================================================================================================================================================'''        



 
# Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras.
def razao_hapax_legomana(palavras):
    return n_palavras_unicas(palavras) / len(palavras)


'''============================================================================================================================================================'''        




 
# Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número
# de sentenças (os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença).
def tamanho_medio_de_sentenca(sentencas):
    caracteres_sentenca = 0
    for sentenca in sentencas:
        caracteres_sentenca = caracteres_sentenca + len(sentenca)
    return caracteres_sentenca / len(sentencas)


'''============================================================================================================================================================'''        




 
# Complexidade de sentença é o número total de frases divido pelo número de sentenças.
def complexidade_de_sentenca(lista_frases, sentencas):
    return len(lista_frases) / len(sentencas)



'''============================================================================================================================================================'''        


 
# Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo
# número de frases no texto (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).
def tamanho_medio_de_frase(lista_frases):
    caracteres_frase = 0
    for frases in lista_frases:
        caracteres_frase = caracteres_frase + len(frases)
    return caracteres_frase / len(lista_frases)





'''============================================================================================================================================================'''        
 
def main():
    assinatura_cp = le_assinatura() #lê a assinatura do aluno infectado com COH-PIAH e retorna a assinatura, que é uma lista contendo os 6 traços linguísticos
    textos_lidos = le_textos()  #lê os textos e retorna uma lista de textos que serão comparados com a assinatura do aluno infectado com COH-PIAH
    avalia_textos(textos_lidos, assinatura_cp) #todos os textos serão comparados com a assinatura do aluno infectado com COH-PIAH para ver qual é mais parecido

main()
