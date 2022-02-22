class Node:
    def __init__(self, value, adj=None):

        self.value = value
        self.adj = adj
        self._print_visited = set()

        if self.adj is None:
            self.adj = []

    def __repr__(self):
        if self in self._print_visited:
            return ''
        else: 
            self._print_visited.add(self)
            final_str = ''
            for n in self.adj:
                final_str += f'{n}\n'

            self._print_visited.remove(self)
            return final_str + f'({self.value}, ({[n.value for n in self.adj]}))'

def deep_copy_graph(graph_node, visited=None):
    if graph_node is None:
        return graph_node
    
    if visited is None:
        visited = {}
    
    if graph_node in visited:
        return visited[graph_node]
    
    visited[graph_node] = Node(graph_node.value, [])

    for node in graph_node.adj:
        visited[graph_node].adj.append(deep_copy_graph(node, visited))

    return visited[graph_node]


n5 = Node(5)
n4 = Node(4)
n3 = Node(3, [n4])
n2 = Node(2)
n1 = Node(1, [n5])
n5.adj = [n3]
n4.adj = [n3, n2]
n2.adj = [n4]

graph_copy = deep_copy_graph(n1)
print(graph_copy)