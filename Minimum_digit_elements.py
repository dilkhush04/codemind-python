n=int(input())
a=list(map(int,input().split()))
temp=999
for i in a:
    i=abs(i)
    i=str(i)
    if(len(i)<temp):
        temp=len(i)
c=0
for i in a:
    i=abs(i)
    i=str(i)
    if(len(i)==temp):
        c=c+1
print(c)