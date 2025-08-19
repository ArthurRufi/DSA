# O que são Arvores Binarias?

## Explicação
Uma arvore binaria é a representação de estrutura de dados em arvore porém sua diferença principal é que cada node tem no **Maximo** duas child nodes.

Como assim?

Imagine o seguinte processo.

Uma arvore que possue um node raiz que corresponde a letra N e seus filhos correspondem a letra A e B.

Logo N tem no maximo dois filhos (chields nodes) que são A e B.

Agora imagine quantos filhos A e B possam ter cada um... 3? 4? Não, o maximo é dois filhos.

    A possui E e I
    B possui C e D

Em sequencia:

    C possui F e G
    D possui H e J
    E possui O e U 
    J possui M 
    I não possui filhos.

Explicando assim fica facil de entender o funcionamento de uma arvore binaria.

Mas uma arvore tem um limite de tamanho, entendendo isso qual o limite de uma arvore?

**O Limite de uma arvore é o numero maximo de arestas do no Raiz _N_ até o último leaf node**

Calma jovem garfanhoto, agora temos a explicação o que é uma _leaf node_

Primeiro temos que diferenciar o que é o tamanho de uma árvore e o que é o limite de uma árvore.
- O limite de uma árvore é determinado pela quantidade de arestas até a ultima folha.
- O tamanho de uma árvore é determinado pela quantidade de nodes que ela possui.

_Notou a diferença?_

No nosso exemplo nossa arvore tem 12 nodes ou seja tamanho = 12

Mas e seu limite de altura?
Nossa maior altura representa o caminho que vai do N (raiz) até o M, quantas arestas será que tem esse espaço? Isso é simples de resolver, dependendo da marcação usada uma árvore pode representar sua raiz como 0 ou como 1. Caso seja 0 com zero nossa árvore tem 3 niveis (raiz, B -> D, D -> J, J -> M) ou 4 se contar a raiz como 1, sendo raiz N e folha (leaf node) M.

## Exemplos
## Aplicação
## Conclusão