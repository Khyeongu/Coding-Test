from sys import stdin

s=list(map(str, stdin.readline().rstrip()))
s.sort()

word=""
number=0

for i in s:
    if 47<ord(i)<58:
        number=number+int(i)
    elif 64<ord(i)<91:
        word=word+i

print(word+str(number))