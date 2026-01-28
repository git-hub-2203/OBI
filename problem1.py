'''
Cifra da Nlogônia
O rei da Nlogônia ordenou que todos os documentos importantes sejam "cifrados", para que apenas quem tem conhecimento da cifra possa lê-los (cifrar um documento significa alterar o original modificando as letras de acordo com algum algoritmo de cifra).

O rei decretou que o seguinte algotimo deve ser usado para cifrar os documentos:

Cada consoante deve ser substituída por exatamente três letras, na seguinte ordem:
a própria consoante (vamos chamar de consoante original);
a vogal mais próxima da consoante original no alfabeto, com a regra adicional de que se a consoante original está à mesma distância de duas vogais, então a vogal mais próxima do início do alfabeto é usada. Por exemplo, se a consoante original é d, a vogal que deve ser usada é e, pois esta é a vogal mais próxima; se a consoante original é c, a vogal que deve ser utilizada é a, porque c está à mesma distância de a e e, e a é mais próxima do início do alfabeto.
a consoante que segue a consoante original, na ordem do início ao fim do alfabeto. Por exemplo, se a consoante original é d, a consoante a ser utilizada é f. No caso de a consoante original ser z, deve ser utilizada a própria letra z.
As vogais não são modificadas.
Nesta tarefa, o alfabeto é
a b c d e f g h i j k l m n o p q r s t u v x z
e as vogais são
a e i o u
Por exemplo, a cifra da palavra "ter" é "tuveros" (tuv-e-ros) e a cifra da palavra "paz" é "poqazuz" (poq-a-zuz).

O rei da Nlogônia procura por alguém que saiba escrever um programa que produza a cifra de uma palavra dada. Você pode ajudá-lo?

Entrada
A primeira e única linha da entrada contém uma palavra P formada por letras minúsculas sem acentuação.

Saída
Seu programa deve produzir uma única linha, contendo a palavra cifrada.

Restrições
A palavra P tem no mínimo uma e no máximo 30 letras, todas minúsculas e sem acentuação.
'''
def cifrar_palavra(palavra):
    # Alfabeto especificado (sem w e y)
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z']
    
    vogais = ['a', 'e', 'i', 'o', 'u']
    
    # Criar dicionário para posições no alfabeto
    posicao = {letra: idx for idx, letra in enumerate(alfabeto)}
    
    resultado = []
    
    for letra in palavra:
        if letra in vogais:
            # Vogais não são modificadas
            resultado.append(letra)
        else:
            # É consoante
            # 1. Primeira letra: a própria consoante
            resultado.append(letra)
            
            # 2. Segunda letra: vogal mais próxima
            pos = posicao[letra]
            
            # Calcular distâncias para todas as vogais
            distancias = []
            for vogal in vogais:
                dist = abs(pos - posicao[vogal])
                distancias.append((dist, vogal))
            
            # Ordenar por distância e, em caso de empate, por ordem alfabética
            distancias.sort(key=lambda x: (x[0], posicao[x[1]]))
            vogal_mais_proxima = distancias[0][1]
            resultado.append(vogal_mais_proxima)
            
            # 3. Terceira letra: próxima consoante no alfabeto
            proxima_pos = pos + 1
            # Encontrar a próxima consoante (pular vogais)
            while proxima_pos < len(alfabeto) and alfabeto[proxima_pos] in vogais:
                proxima_pos += 1
            
            if proxima_pos >= len(alfabeto):
                # Se não houver próxima consoante, usar 'z' (ou a própria se for 'z')
                if letra == 'z':
                    resultado.append('z')
                else:
                    resultado.append('z')
            else:
                resultado.append(alfabeto[proxima_pos])
    
    return ''.join(resultado)

# Leitura da entrada
P = input().strip()

# Gerar e imprimir a cifra
print(cifrar_palavra(P))




