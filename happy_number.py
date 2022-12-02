def happy(n):
    s=0
    while(n!=0):
        rem=n%10
        s+=rem*rem
        n//=10
    return s
n=int(input())
n=happy(n)
while(1>0):
    if n<10:
        if n==1 or n==7:
            print("True")
            break
        else:
            print("False")
            break
    else:
        n=happy(n)