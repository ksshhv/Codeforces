import math
x=int(input())
k=x
l=[]
while(x):
    a1=list(map(int,input().split()))
    l.append(a1)
    x-=1
a1=math.sqrt((l[0][1]*l[0][2])//l[1][2])
z=1
print(int(a1),end=" ")
while(z<k):
    print(int(l[0][z]//a1),end=" ")
    z+=1
