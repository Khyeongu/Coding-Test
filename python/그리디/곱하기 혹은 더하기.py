from sys import stdin

s=list(map(int, stdin.readline().rstrip()))
total=0

for i in s:
    if total<=1 or i<=1:
        total=total+i
    else:
        total=total*i

print(total)

