n=int(input())
a=list(map(int,input().split()))[:n]
def rev(n):
    rev1=0
    m=n
    while(n!=0):
        rev1=rev1*10+n%10
        n//=10
    n=m
    return rev1
for i in a:
    print(rev(i),end=" ")
    