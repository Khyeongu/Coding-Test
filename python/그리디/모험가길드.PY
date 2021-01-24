from sys import stdin

n=int(stdin.readline().rstrip())
x=list(map(int, stdin.readline().rstrip().split()))
count=0
member=0

x.sort()

for i in x:
    member+=1
    if(member>=i):
        count+=1
        member=0
print(count)
