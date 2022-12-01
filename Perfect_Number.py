def perfact(n):
    c=0
    for i in range(1,n):
        if n%i==0:
            c=c+i
    return c
n=int(input())
if n==perfact(n):
    print("True")
else:
    print("False")