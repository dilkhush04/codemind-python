n=int(input())
s=0
a=list(map(int,input().split()))
for i in range(n):
    s=s+a[i]
ave=int(s/n)
if ave in a:
    print("True")
else:
    print("False")