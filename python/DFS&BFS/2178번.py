from sys import stdin
from collections import deque

x, y = map(int, stdin.readline().rstrip().split())

maze=[]
distance=0

for _ in range(x):
    maze.append(list(map(int, stdin.readline().rstrip())))

dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

queue=deque()
queue.append([0,0])
while queue:
    n,m=queue.popleft()
    for i in range(4):
        nx=n+dx[i]
        ny=m+dy[i]
        if nx==0 and ny==0:
            continue
        if nx<0 or nx>=x or ny<0 or ny>=y:
            continue
        if maze[nx][ny]==0:
            continue
        if maze[nx][ny]==1:
            maze[nx][ny]=maze[n][m]+1
            queue.append([nx,ny])

print(maze[x-1][y-1])