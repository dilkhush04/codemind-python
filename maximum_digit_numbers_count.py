def number(n):
    c=0
    if n<0:
        n=-n
    if n==0:
        return 1
    while(n):
        c=c+1
        n//=10
    return c


n=int(input())
a=list(map(int,input().split()))
c=[]
for i in a:
    c.append(number(i))
ln=max(c)

for i in a:
    if number(i)==ln:
        print(i,end=" ")
