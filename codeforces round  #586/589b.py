h,w=map(int,input().split())
w1=w
h1=h+1
b=[]
rv=list(map(int,input().split()))
cv=list(map(int,input().split()))
while(h1):
    w1=w+1
    a=[]
    while(w1):
        a.append(0)
        w1-=1
    b.append(a)
    h1-=1
#print(b)
s=0
while(s<len(rv)):
    f=rv[s]
    while(f>=0):
        b[s][f]=1
        f-=1
    s+=1
#print(b)
s=0
while(s<len(cv)):
    f=cv[s]
    while(f>=0):
        b[f][s]=1
        f-=1
    s+=1
w1=w-1
#print(b)
c=0
h-=1
while(h>=0):
    w1=w-1
    while(w1>=0):
        if(b[h][w1]==0):
            c+=1
        w1-=1
    h-=1
if(c==0):
    print(0)
else:
    pr
