from sys import stdin

n, value=map(int,stdin.readline().rstrip().split())
coin=[]
for j in range(n):
    coin.append(int(stdin.readline().rstrip()))

coin.sort(reverse=1)
total=0

for i in range(len(coin)):
    if i<n:
        total=total+value//coin[i]
        value=value%coin[i]

print(total)



