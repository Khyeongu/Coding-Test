from sys import stdin

direction=str(stdin.readline().rstrip())
count=0

num_direction=[]
num_direction.append(ord(direction[0]))
num_direction.append(direction[1])

move=[[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]

for i in range(len(move)):
    move[i][0]+=int(num_direction[0])
    move[i][1]+=int(num_direction[1])

for j in move:
    if 96<j[0]<105 and 0<j[1]<9:
        count+=1

print(count)