s=input()
k=0
for i in s:
    if i=='(':
        k=k+1
    if i==')':
        k=k-1
    if k<0:
        break
if(k==0):
    print("True")
else:
    print("False")