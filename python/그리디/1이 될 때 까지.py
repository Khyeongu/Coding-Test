from sys import stdin

n, k=map(int, stdin.readline().rstrip().split())

count=0

while n>1 :
    target=(n//k)*k
    count=count+(n-target)
    n=target

    if n<k:
        break

    n=n//k
    count+=1

count=count+(n-1)
print(count)
