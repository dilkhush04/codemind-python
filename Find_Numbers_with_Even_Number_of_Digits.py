def Digit(n):
    c=0
    while(n!=0):
        c=c+1
        n//=10
    if(c%2==0):
        return 1
    else:
        return 0
n=int(input())
c=0
a=list(map(int,input().split()))
for i in a:
    if Digit(i)==1:
        c=c+1
print(c)