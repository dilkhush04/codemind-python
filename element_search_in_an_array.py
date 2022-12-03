n=int(input())
flag=0
a=list(map(int,input().split()))
key=int(input())
for i in range(n):
    if a[i]==key:
        flag=1
if(flag==1):
    print("True")
else:
    print("False")