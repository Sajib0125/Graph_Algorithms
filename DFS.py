graph1 = {
    1 : [2,3],
    2 : [4,5],
    4 : [6],
    6 :[],
    3 :[],
    5 :[]
}

def DFS(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            DFS(graph, n, visited)
    return visited


print(DFS(graph1,1, []))