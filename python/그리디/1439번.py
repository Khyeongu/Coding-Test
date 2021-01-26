from sys import stdin

s=list(map(str,stdin.readline().rstrip()))

for i in range(len(s)):
    if i==0:
        prev=s[i]
        continue
    
    if prev==s[i]:
        s[i-1]="d"
        continue
    
    if prev!=s[i]:
        prev=s[i]
        
print(min(s.count("1"), s.count("0")))
    