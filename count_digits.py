n=int(input())
a=list(map(int,input().split()))
for i in a:
    i=abs(i)
    i=str(i)
    print(len(i),end=" ")