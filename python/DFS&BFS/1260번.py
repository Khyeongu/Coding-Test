from sys import stdin
from collections import deque

n,m,v=map(int,stdin.readline().rstrip().split())
graph=[[]*0 for _ in range(n+1)]
dfs_visited=[False]*(n+1)
bfs_visited=[False]*(n+1)

def dfs(graph,v,dfs_visited):
    dfs_visited[v]=True
    print(v, end=" ")

    for i in graph[v]:
        if not dfs_visited[i]:
            dfs(graph,i,dfs_visited)

def bfs(graph,v,bfs_visited):
    queue=deque([v])
    bfs_visited[v]=True

    while queue:
        t=queue.popleft()
        print(t, end=" ")
        for i in graph[t]:
            if not bfs_visited[i]:
                queue.append(i)
                bfs_visited[i]=True

for _ in range(m):
    a,b=map(int, stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

dfs(graph,v,dfs_visited)
print()
bfs(graph,v,bfs_visited)

