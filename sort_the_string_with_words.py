def sortString(str) :
    str = ' '.join(sorted(str))
    return str
s = input()
s=s.split(" ")
print(sortString(s))