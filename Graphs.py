class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex is self.adj_list.keys():
            for v in self.adj_list[vertex]:
                self.adj_list[v].remove(vertex)
            self.adj_list.pop(vertex)
            return True
        return False
    
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])
    
my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')
print("*"*30)
my_graph.add_edge('A', 'B')
my_graph.add_edge('C', 'D')
my_graph.print_graph()
print("*"*30)
my_graph.add_edge('A', 'C')
my_graph.add_edge('B', 'D')
my_graph.print_graph()
print("*"*30)
my_graph.remove_edge('A', 'B')
my_graph.print_graph()
print("*"*30)
my_graph.remove_vertex('D')
my_graph.print_graph()