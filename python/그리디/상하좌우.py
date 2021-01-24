from sys import stdin

n=int(stdin.readline().rstrip())
direction=list(map(str, stdin.readline().rstrip().split()))

x, y= 1,1
move_types=['U', 'D', 'L', 'R']
dx=[0,0,-1,1]
dy=[-1,1,0,0]

for d in direction:
    for i in range(len(move_types)):
        if(d==move_types[i]):
            nx=x+dx[i]
            ny=y+dy[i]
    if(nx<1 or nx>n or ny<1 or ny>n):
        continue
    x,y=nx,ny

print(x,y)