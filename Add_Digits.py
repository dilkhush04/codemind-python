def add(n):
    s=0
    while(n!=0):
        s+=n%10
        n//=10
    return s
n=int(input())
n=add(n)
while(1>0):
    if(n<10):
        print(n)
        break
    else:
        n=add(n)