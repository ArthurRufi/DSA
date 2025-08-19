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

### Mas isso não é uma lista ligada?
Não e sim, na verdade são bem parecidos os conceitos e inclusive se confude também com Matrizes.
Árvore binaria é no final das contas quase como um megazorde dos dois conceitos usando o melhor de ambos.

De modo geral listas ligadas ou listas encadeadas são rapidas I/O de dados porém são lentas para acessar dado que precisa ser percorrida. 

Já as matrizes são excelentes para consultas mas alocar memoria ao fazer I/O de dados é custoso porque precisa que elementos sejam movidos de lugar para dar lugar ou assumir lugar de outros.

Então é nesse ponto que a **árvore binaria** brilha!
Elas são ótimas quando comparadas a matrizes e listas vinculadas porque são TANTO rápidas no acesso a um nó quanto rápidas na hora de excluir ou inserir um nó, sem necessidade de deslocamentos de memória.

## Tipos
Nessa altura do campeonato vou levantar somente 3 tipos de árvores e cabe a você, jovem garfanho, procurar outros tipos e exemplos.

Os tipos que vamos utilizar nesse artigo serâo:
- Balanced
- Full
- Complete and Balanced

E vamos para os conceitos de cada uma 

### Conceitos de Tipos de Árvores
1. Balanced: tem no máximo 1 de diferença entre as alturas das subárvores esquerda e direita, para cada node na subarvore.
2. Full: é um tipo de árvore em que cada nó tem 0 ou 2 nós filhos.
3. Complete and Balanced: Possui todos os níveis cheios de nós, exceto o **último nível**, que também pode ser completo, ou seja, preenchido da esquerda para a direita. As propriedades de uma Árvore Binária completa significam que ela também é balanceada.

## Exemplos
## Aplicação
## Conclusão