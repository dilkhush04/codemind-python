def Harsh(n):
    m=n
    s=0
    while(m!=0):
        rem=m%10
        s=s+rem
        m//=10
    if n%s==0:
        return 1
    else:
        return 0
n=int(input())
if Harsh(n)==1:
    print("True")
else:
    print("False")