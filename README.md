# Componentes Biconexas

Este é um programa em python que dado um grafo não direcionado atráves de algum arquivo .txt ele retorna as componentes biconexas e articulações do grafo e informações dos vértices como low, demarcadores a partir de uma dfs com raiz definida no arquivo .txt

## Requisitos

- Python

## Como rodar o programa
    python componentesBiconexas.py < input.txt

## Exemplo

### Entrada (input.txt):
Primeira linha é:
**número_de_vértices raiz_da_dfs**

As linhas restantes são as arestas do grafo em **ordem alfabética (importante!)**

```
8 a
a b
a c
a h
b c
b d
b f
b g
c g
d f
e f
```

### Saída:
```
-----------------------
Graph:
[a]: b, c, h
[b]: a, c, d, f, g
[c]: a, b, g
[d]: b, f
[e]: f
[f]: b, d, e
[g]: b, c
[h]: a
-----------------------
Parent
[a]: a
[b]: a
[c]: b
[d]: b
[e]: f
[f]: d
[g]: c
[h]: a
-----------------------
Height
[a]: 0
[b]: 1
[c]: 2
[d]: 2
[e]: 4
[f]: 3
[g]: 3
[h]: 1
-----------------------
Low
[a]: a
[b]: a
[c]: a
[d]: b
[e]: e
[f]: b
[g]: b
[h]: h
-----------------------
Demarc
[a]: True
[b]: True
[c]: False
[d]: True
[e]: True
[f]: False
[g]: False
[h]: True
-----------------------
Artic
[a]: True
[b]: True
[c]: False
[d]: False
[e]: False
[f]: True
[g]: False
[h]: False
-----------------------
Componentes Biconexas
{e, f}
{f, d, b}
{h, a}
{g, c, b, a}
```

