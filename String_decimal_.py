n=int(input())
a=[]
for i in range(n):
    s=input()
    if s.isdigit():
        a.append(1)
    else:
        a.append(0)
for i in range(n):
    if(a[i]==1):
        print("True")
    else:
        print("False")
        