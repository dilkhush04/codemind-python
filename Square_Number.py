n=int(input())
k=0
for i in range(n):
    for j in range(i+1,n):
        if((i**2+j**2)==n):
            k=k+1
            print("True")
            break
    if(k>0):
        break
if(k==0):
    print("False")