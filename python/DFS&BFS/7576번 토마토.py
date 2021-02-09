from sys import stdin
from collections import deque

n,m=map(int, stdin.readline().rstrip().split())
box=[]
check_zero=0

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs():
    queue=deque()
    for i in range(m):
        for j in range(n):
            if box[i][j]==1:
                queue.append([i,j])
                
    while queue:
        x,y=queue.popleft()
        
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if box[nx][ny]==0:
                box[nx][ny]=box[x][y]+1
                queue.append([nx,ny])
    return box
        

for _ in range(m):
    box.append(list(map(int, stdin.readline().rstrip().split())))
    
for b in bfs():
    if 0 in b:
        check_zero+=1
        
if max(map(max, box))==-1:
    print(0)
elif check_zero!=0:
    print(-1)
else:
    print(max(map(max, box))-1)