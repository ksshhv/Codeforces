rs=int(input())
dol=int(input())
euro=int(input())
mindol=dol
mineuro=euro*5
m=0
minde=0
mined=[]
#while(m<=rs//mindol):
#    l=rs-mindol*m
#    minde.append(l%mineuro)
#    m+=1
minde=rs%mindol
n=0
while(n<=rs//mineuro):
    k=rs-mineuro*n
    mined.append(k%mindol)
    n+=1
print(min(minde,min(mined)))
