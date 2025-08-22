# O que são Arvores Binarias?

## Referencias para estudos
- [VIDEO: Programação Dinâmica](https://www.youtube.com/watch?v=NpJVZtgSY4U&list=PL5TJqBvpXQv7ipm2exZbbqwpFZc-TZ80s)
- [VIDEO: Árvore binária em 5 minutos com Java](https://youtu.be/V3T67I9zuNw?si=boHoLvu-85l_M3sB)
- [ARTIGO: Wikipedia](https://pt.wikipedia.org/wiki/%C3%81rvore_bin%C3%A1ria)
- [ARTIGO: Elemar Jr](https://elemarjr.com/clube-de-estudos/artigos/introducao-a-arvore-binaria-conceitos-terminologias-e-implementacao/)

![](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbHo1MXZkZTI4cWo4YjY1bG5pbnkycm5maWcyajV4NWJqbWl1cXNqYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Vi5TUmZz8LZb95j2xb/giphy.gif)
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
1. **Balanced** : tem no máximo 1 de diferença entre as alturas das subárvores esquerda e direita, para cada node na subarvore.
2. **Full**: é um tipo de árvore em que cada nó tem 0 ou 2 nós filhos.
3. **Complete and Balanced**: Possui todos os níveis cheios de nós, exceto o **último nível**, que também pode ser completo, ou seja, preenchido da esquerda para a direita. As propriedades de uma Árvore Binária completa significam que ela também é balanceada.

## Exemplos
```python
class RamosDaArvore:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = RamosDaArvore('R')
ramoA = RamosDaArvore('A')
ramoB = RamosDaArvore('B')
ramoC = RamosDaArvore('C')
ramoD = RamosDaArvore('D')
ramoE = RamosDaArvore('E')
ramoF = RamosDaArvore('F')
ramoG = RamosDaArvore('G')
```
Acima foi definido o a arvore e seus ramos (nodes) mas cada node tem 2 ou 1 ramo, como nosso software vai saber sobre esses ramos?

De modo grosseiro e nada refinado, ele vai ser tratado e declarado da forma abaixo:
```python
root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG
```

O que raios vai acontecer agora?

É left e right para todo lado que estou perdido, o que fazer?

Calma jovem garfanhoto, aqui está tua explicação:


```
O root já tem definido o left e rigth, sendo o ramo a esquerda o nodeA e o ramo a diretia o node B fazendo a seguinte proporção:

    root.left = nodeA
    root.right = nodeB

    
------------------------------------------------------------------------------

                                root
                               /    \
                           nodeA    nodeB
```

Legal, concorda?

Vamos para o restante:
```
    root.left = nodeA
    root.right = nodeB

    nodeA.left = nodeC
    nodeA.right = nodeD
     
------------------------------------------------------------------------------

                                root
                               /    \
                              /      \
                          nodeA       nodeB
                         /     \
                        /       \
                    nodeC      nodeD
```
Agora parece que está melhorando o entendimento da dinamica:
```
    root.left = nodeA
    root.right = nodeB

    nodeA.left = nodeC
    nodeA.right = nodeD
     
    nodeB.left = nodeE
    nodeB.right = nodeF

    nodeF.left = nodeG
------------------------------------------------------------------------------

                                  root
                               /         \
                              /           \
                             /             \
                        nodeA               nodeB
                       /     \             /     \
                      /       \           /       \
                     /         \         /         \ 
                nodeC          nodeD | nodeE        nodeF
                                        /
                                       /
                                    nodeG   

```
Agora sim, consegue visualizar com codigo e grafico como ocorre a construção de uma arvore? Mesmo não estatando exemplificado com sua melhor correspondencia tecnica de codigo.

Podemos refinar mais o codigo ao decorrer do curso.


## Aplicação
Agora que já sabemos o que é uma arvore, como ela é construida e como isso vai ser definido no nosso codigo de forma geral, vamos agora entender as aplicações praticas e algoritmicas.

### Percorrer uma Arvore Binaria?

Quando queremos percorrer uma arvore binaria temos situações diversas entretanto vamos ficar com as mais populares.

- Busca em Largura
- Busca em Profundidade 

#### Busca Em Largura

A busca em largura, de forma resumida é quando os nós que estão no mesmo nivel são consultados antes de passar para um proximo nivel, sendo assim a arvore é explorada de forma horizontal.

#### Busca em profundidade 

A busca em profundidade é mais especifica para percorrer a partir de um node, ele vai percorrer galho por galho até acabar aquele galho e passar para o proximo galho.

## Conclusão

Futuramente teremos modulos para aprofundar os estudos nas buscas em arvores binarias.

Para concluir, as arvores binarias são popularmente usadas na computação e desenvolvimento quando precisamos armazernar urls de forma hierarquica, hierarquia de sites, busca com pré requisitos e ligações e até mesmo em organograma familiar.