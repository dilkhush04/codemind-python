n=int(input())
test_list = list(map(int,input().split()))
res = sum(list(set(test_list)))
print (str(res))