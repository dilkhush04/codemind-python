n=int(input())
a=list(map(int,input().split()))
b=0
for i in a:
    i=abs(i)
    i=str(i)
    if(len(i)>b):
        b=len(i)
c=0
d=0
for i in a:
    i=abs(i)
    i=str(i)
    if(len(i)==b):
        d=d+1
print(d)