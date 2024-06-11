class Graph:
    def __init__(self,num):
        self.V = num
        self.graph=[None]*self.V

    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[s]
        self.graph[d] = node

    def print_graph(self):
        for i in eange(self.v):
            print("Vertex"+str(i)+":",end="")
            temp  = self.graph[i]
            while temp:
                print("->{}".format(temp.vertex),end="")
                temp = temp.next
            print("\n")

graph = {("0","1"),("0","2"),("0","3"),("2","1")}
g=Graph(graph)
print(g.print_graph)
