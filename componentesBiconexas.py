import sys

class Vertex:
    def __init__(self, name):
        if len(name) != 1:
            raise ValueError("O argumento 'char' deve ser uma string de comprimento 1")
        self.name = name # Ex: Vertex 'a'
        self.neighbors = [] # Vizinhos do vértice
        self.visited = False
        self.low = self
        self.demarc = False
        self.artic = False

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def update_height(self, new_height):
        self.height = new_height
    
    def update_visited(self, value):
        self.visited = value

    def update_low(self, low):
        self.low = low

    def update_parent(self, parent):
        self.parent = parent

    def update_demarc(self, value):
        self.demarc = value

    def update_artic(self, value):
        self.artic = value



class Graph:
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.vertex_dict = {}
        self.dfs_index = 0
        
    def print_graph(self):
        print("-----------------------")
        print("Graph:")
        for vertex in self.vertex_dict.values():
            print(f"[{vertex.name}]: {', '.join(neighbor.name for neighbor in vertex.neighbors)}")
        print("-----------------------")
        print("Parent")
        for vertex in self.vertex_dict.values():
            print(f"[{vertex.name}]: {vertex.parent.name}")
        print("-----------------------")
        print("Height")
        for vertex in self.vertex_dict.values():
            print(f"[{vertex.name}]: {vertex.height}")
        print("-----------------------")
        print("Low")
        for vertex in self.vertex_dict.values():
            print(f"[{vertex.name}]: {vertex.low.name}")
        print("-----------------------")
        print("Demarc")
        for vertex in self.vertex_dict.values():
            print(f"[{vertex.name}]: {vertex.demarc}")
        print("-----------------------")
        print("Artic")
        for vertex in self.vertex_dict.values():
            print(f"[{vertex.name}]: {vertex.artic}")
        print("-----------------------")
        print("Componentes Biconexas")
        for i in self.componentes:
            component_str = "{" + ", ".join(j.name for j in i) + "}"
            print(component_str)

    def add_edge(self, a, b):
        if len(a) != 1 or len(b) != 1:
            raise ValueError("Error: add_edge() String de comprimento 1")
        
        if a not in self.vertex_dict:
            self.vertex_dict[a] = Vertex(a)
        if b not in self.vertex_dict:
            self.vertex_dict[b] = Vertex(b)

        self.vertex_dict[a].add_neighbor(self.vertex_dict[b])
        self.vertex_dict[b].add_neighbor(self.vertex_dict[a])

    def componentes_biconexas(self, vertex_entrada):
        self.vertex_raiz = self.vertex_dict[vertex_entrada]
        self.vertex_raiz.update_height(0) # Atualiza a altura da raiz para 0
        self.vertex_raiz.update_parent(self.vertex_raiz) # Torna o pai da raiz ela mesma
        self.stack = []
        self.componentes = []

        def dfs(vertex):
            if not isinstance(vertex, Vertex):
                raise ValueError("Error: não é um objeto da classe Vertex")
            self.stack.insert(0, vertex)
            vertex.update_visited(True)
            vertex.update_low(vertex) # Atualiza o low do vértice para ele mesmo
            for neighbor in self.vertex_dict[vertex.name].neighbors:
                if neighbor.visited == False:
                    neighbor.parent = vertex # Atualiza o pai do vizinho inserindo ele na árvore
                    neighbor.height = vertex.height + 1
                    dfs(neighbor)
                if neighbor.visited == True and neighbor != vertex.parent:
                    # Visitar aresta de retorno, atualizar o low se for menor
                    if (neighbor.height < vertex.height):
                        vertex.low = neighbor

            # Ao sair do vértice, caso o meu pai tenha low pior que o meu, eu atualizo o low do meu pai para o meu low
            if (vertex.low.height < vertex.parent.low.height):
                vertex.parent.low = vertex.low

            # Verifica se o vértice é demarcador
            if vertex.low == vertex or vertex.low == vertex.parent:
                vertex.update_demarc(True)
                if vertex.parent != self.vertex_raiz:
                    vertex.parent.update_artic(True)

            # Verifica se a raiz tem mais de 1 filho
            if vertex.parent == self.vertex_raiz:
                count = 0
                for v in self.vertex_dict.values():
                    if hasattr(v, 'parent'):
                        if v.parent == self.vertex_raiz:
                            count = count + 1
                if count > 2:
                    self.vertex_raiz.update_artic(True)

            # Componentes biconexas
            if vertex.demarc and vertex.parent.artic and vertex != self.vertex_raiz and self.stack:
                componente = []
                while self.stack[0] != vertex:
                    componente.append(self.stack.pop(0))
                componente.append(self.stack.pop(0))
                componente.append(vertex.parent)
                self.componentes.append(componente)


        dfs(self.vertex_dict[vertex_entrada])

        # Jogar o resto da pilha em uma Componente Biconexa
        if self.stack:
            componente = []
            while self.stack:
                componente.append(self.stack.pop(0))
            self.componentes.append(componente)


    def ordenarGraph(self):
        self.vertex_dict = dict(sorted(self.vertex_dict.items()))


    
if __name__ == "__main__":
    data = sys.stdin.read()
    edges = data.split('\n')
    args = edges.pop(0)
    n, raiz = args.split(' ')
    
    graph = Graph(int(n))

    for i in range(len(edges)):
        a, b = edges[i].split(' ')
        graph.add_edge(a, b)


    graph.ordenarGraph() # Ordena o dicionário em ordem alfabética
    # graph.print_graph() # Printa o gráfico

    graph.componentes_biconexas(raiz)
    graph.print_graph() # Printa o gráfico
