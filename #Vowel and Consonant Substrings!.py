def isVowel(char):
    return True if char in ['a','e','i','o','u'] else False

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, s):
        v = 0
        c = 0
        ans = 0
        for i in range(0,len(s)):

            if isVowel(s[i]) and c > 0:
                ans += c

            elif isVowel(s[i]) == False and v > 0:
                ans += v
            
            v += 1 if isVowel(s[i]) else 0
            c += 1 if isVowel(s[i])==False else 0

        return ans%((10**9)+7)

            
