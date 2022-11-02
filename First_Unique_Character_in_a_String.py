class Solution(object):
   def firstUniqChar(self, s):
      frequency = {}
      for i in s:
         if i not in frequency:
            frequency[i] = 1
         else:
            frequency[i] +=1
      for i in range(len(s)):
         if frequency[s[i]] == 1:
            return i
      return -1
ob1 = Solution()
s=input()
print(ob1.firstUniqChar(s))
