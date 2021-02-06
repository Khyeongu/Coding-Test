from sys import stdin
from collections import deque

n = int(stdin.readline().rstrip())
graph = []
count_list = []
count = 0


def bfs(x, y):
    queue = deque()
    queue.append([i, j])
    count = 0
    while queue:
        x, y = queue.popleft()

        if graph[x][y] == 1:
            graph[x][y] = 0
            count += 1

            for k in range(4):
                nx = x+dx[k]
                ny = y+dy[k]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if graph[nx][ny] == 0:
                    continue
                if graph[nx][ny] == 1:
                    queue.append([nx, ny])

    if count!=0:
        count_list.append(count)
    return 0


for _ in range(n):
    graph.append(list(map(int, stdin.readline().rstrip())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    for j in range(n):
        bfs(i, j)


print(len(count_list))
for c in sorted(count_list):
    print(c)
