# Binary Search (Busca Binária)

## Referencias para estudos
- [Livro: Entendendo Algoritmos; Aditya Y. Bhargava]()
- [Artigo: W3 School](https://www.w3schools.com/dsa/dsa_algo_binarysearch.php)
- [Curso Gratis: estrutura de dadosestrutura de dados](https://www.coursera.org/learn/data-structures)
- [Video: Augusto Galego - Busca Binária](https://youtu.be/zSyV0VaTF3k)






## O que é Binary Search?
    Para entender busca binária primeiro você deve entender o que é um array


Imagine agora que você precisa encontrar um numero de um apartamento em um condominio, cada apartamento fica em um bloco e é definido os numeros da seguinte forma.

O primeiro numero é numero do bloco que pode variar de 1 até 9, os outros dois numeros são correpondente ao numero do apartamento.

    Apartamento 306 >>>>> Bloco 3 >>>>>> Apartamento 06

Então um array com os apartamentos ficará aproximadamente assim:

```
[301, 302, 303, 304, 305, 306, 307, 308] e assim por diante
```

Agora imagine fazer a pesquisa de um item dentro desse array que vai do 101 até o 918... Vai ser demorado e custoso, concorda?

Caso sejá necessario consultar uma lista apartamentos ocupados que vão de 101 até 918 e dessa lista seja necessario encontrar o numero de um apartamento especifico, isso vai ser custo sempre estar fazendo um loop for para iterar item a item até chegar no numero final.

Caso deseje o numero 718, como encontrar esse numero e ver se ele está ocupado ou não?

```python
occupied_apartment = [101, 103, 104, 106, 201, 202, 204, 205, 206, 207, 212, 215, 216, 217, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918]

for apartament in occupied_apartment:
    if apartment == 217:
    return True
```

**Isso vai ser _custoso_ e _demorado_!**

A lista entregue foi relativamente grande, agora imagine milhares de itens em uma lista para ser iterados 1 a 1 até encontrar o resultado... ~~Errado e lento~~

Podemos sim fazer de   uma forma mais eficiente e se chama **_BUSCA BINARIA_**

### Explicação de Codigo

```python
    occupied_apartment = [101, 103, 104, 106, 201, 202, 204, 205, 206, 207, 212, 215, 216, 217, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918]

    def binarySearch(lista, valorProcurado):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        numeroMeio = (inicio + fim) // 2

        if lista[numeroMeio] == valorProcurado:
            return numeroMeio
        
        if lista[numeroMeio] < valorProcurado:
            inicio = numeroMeio + 1
        else:
            fim = numeroMeio - 1

    return -1

```

Não entendi nada, o que aconteceu nesse codigo?

```python
   def binarySearch(lista, valorProcurado):
    inicio = 0
    fim = len(lista) - 1 

```
Inicia nossa função, determinando o valor de inicio da lista e o valor final da lista (em relação ao tamanho da lista e não ao valor inicial e final)

Essa parte é de grande importancia pois com ela vai ser determinado a base da busca binaria.

```python
   while inicio <= fim:
        numeroMeio = (inicio + fim) // 2

        if lista[numeroMeio] == valorProcurado:
            return numeroMeio
        
        if lista[numeroMeio] < valorProcurado:
            inicio = numeroMeio + 1
        else:
            fim = numeroMeio - 1

    return -1 
```
Vamos a primeira linha:
```python
    while inicio <= fim:
```
O loop while executa enquanto inicio for menor ou igual a fim. Quando inicio ultrapassa fim, significa que o elemento não foi encontrado
```python
    numeroMeio = (inicio + fim) // 2
```
Nesse ponto o _numeroMeio_ corresponde à posição do meio do array, isso vai ser importante para ir alocando os ponteiros.
```python
        if lista[numeroMeio] == valorProcurado:
            return numeroMeio
```
Na condicional acima conseguimos observar o primeiro comportamento de confirmação do algoritmo binary search e aonde tudo começa a tomar logica. 

O **_if_** vai fazer a confirmação de se o item na posição _numeroMeio_ é igual ao valor procurado, caso seja a função vai retornar a posição do item e não o item (você pode retornar o item)
```python
        if lista[numeroMeio] < valorProcurado:
            inicio = numeroMeio + 1
```
Agora observamos a primeira alocação de ponteiro do nosso codigo, o **if** faz a condicional e caso o _numeroMeio_ for **_MENOR_** que o _valorProcurado_ o ponteiro _inicio_ vai ser alocado para a posição _numeroMeio_ + 1, assim gerando artificialmente um novo array sem necessariamente criar um novo array.

Um array menor, com menos itens ~~inúteis~~ e menor custo computacional.

```python
        else:
            fim = numeroMeio - 1
```            
Agora vamos ver o else... Esse else poderia facilmente ser um:
```python
        if lista[numeroMeio] > valorProcurado:
            fim = numeroMeio - 1
```
Ambos funcionariam bem, mas vamos manter a explicação final e não a condicional

Essa é a segunda alocação de ponteiro, agora com o ponteiro _fim_, caso o item da lista na posição _numeroMeio_ seja maior que o _valorProcurado_ o ponteiro _fim_ vai diminuir o **tamanho do array** agora tirando a **metade final** daquele array criando um novo array artificial sem gerar um novo espaço de memoria relativo à um array, gerando assim menor custo computacional.

## Conclusão

A busca binária é mais eficiente que a busca linear em listas ordenadas porque a cada passo descarta metade dos elementos restantes, enquanto a busca linear descarta apenas um por vez. Também não precisa criar novos espaços de memoria criando novos arrays, com os ponteiros é facil escalar e percorrer array sem ferir a notação Big O de forma exponencial.
