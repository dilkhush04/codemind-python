def checkValidString(s):
    star= 0
    leftparen = 0
    for ch in s:
        if ch=='(':
            leftparen += 1
        elif ch=='*':
            star += 1
        elif ch==')':
            leftparen -= 1
            if -leftparen>star:
                return False
    if abs(leftparen)>star:
        return False
    
    star = 0
    rightparent = 0
    for i in range(len(s)-1,-1,-1):
        if s[i]==')':
            rightparent += 1
        elif s[i]=='*':
            star += 1
        elif s[i]=='(':
            rightparent -= 1
            if -rightparent>star:
                return False
    if abs(rightparent)>star:
        return False
    return True

s=input()
print(checkValidString(s))
    