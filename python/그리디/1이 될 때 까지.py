from sys import stdin

n, k=map(int, stdin.readline().rstrip().split())

count=0

while n>1 :
    if n%k==0 :
        n=n//k
        count=count+1
    else :
        n=n-1
        count=count+1

print(count)
