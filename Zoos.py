lst=input()
k=0
k1=0
for i in range(len(lst)):
    if(lst[i]=='z'):
        k=k+1
    else:
        k1=k1+1
if((k*2)==k1):
    print("Yes")
else:
    print("No")