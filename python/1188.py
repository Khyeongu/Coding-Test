from sys import stdin
from math import gcd

n, m=map(int, stdin.readline().rstrip().split())

d=gcd(n,m)

n,m=n//d, m//d

print(d*(m-1))


