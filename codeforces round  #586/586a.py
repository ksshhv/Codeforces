x=int(input())
y=input()
z=0
coutz=0
coutn=0
while(z<x):
    if(y[z]=='z'):
        coutz+=1
    if(y[z]=='n'):
        coutn+=1
    z+=1
while(coutn):
    print("1", end=" ")
    coutn-=1
while(coutz):
    print("0", end=" ")
    coutz-=1
