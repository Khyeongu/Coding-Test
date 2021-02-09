from sys import stdin
from collections import deque

n, k=map(int, stdin.readline().rstrip().split())
visited=[0]*100001

def bfs(n,k,visited):
    queue=deque()
    queue.append(n)
    visited[n]=1

    while queue:
        x=queue.popleft()
        if x==k:
            break
        for nx in (x-1, x+1, 2*x):
            if 0<=nx<=100000 and visited[nx]==0:
                queue.append(nx)
                visited[nx]=visited[x]+1
    print(visited[x]-1)

bfs(n,k,visited)