n=int(input())
num=0
if n>0:
    while(n!=0):
        num=num*10+n%10
        n//=10
    print(num)
else:
    n=-n
    while(n!=0):
        num=num*10+n%10
        n//=10
    print(-num)