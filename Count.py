n=int(input())
lst=list(map(int, input().split()))
odd=0
even=0
for i in lst:
    if(i%2==0):
        even+=1
    else:
        odd+=1
print(even,odd)