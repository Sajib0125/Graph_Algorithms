import collections

def BFS(graph, root):
    seen, queue = set(), collections.deque([root])
    while (queue):
        vertex = queue.popleft()
        visited(vertex)
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)

def visited(n):
    print(n,end=' ')


graph = {0: [1,2], 1: [2,3], 2: [4,5],3:[4],4:[],5:[]}
BFS(graph, 0)