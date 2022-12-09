n=int(input())
lst=[]
lst1=list(map(int, input().split()))
for x in lst1:
    if(x not in lst):
        lst.append(x)
if(len(lst)<=3):
    print(lst[-1])
else:
    print(lst[2])