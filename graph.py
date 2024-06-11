vertices = {"0","1","2","3"}
edges = {("0","1"),("0","2"),("0","3"),("2","1")}
graph = dict()
for vertex in vertices :
    graph [vertex] = []
for edge in edges :
    v1  = edge [0]
    v2 = edge [1]
    graph[v1].append(v2)
    graph[v2].append(v1)

print ("Himpunan vertex:", vertices)
print ("Himpunan edge:", edges)
print ("representasi graph :")
print (graph)
