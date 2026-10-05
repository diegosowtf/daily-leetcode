import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        gcd_length = math.gcd(len(str1), len(str2))
        return str1[:gcd_length]

sol = Solution()
print(sol.gcdOfStrings("ABCABC", "ABC"))      
print(sol.gcdOfStrings("ABABAB", "ABAB"))     
print(sol.gcdOfStrings("LEET", "CODE")) 

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        a, b = len(str1), len(str2)
        while b:
            a, b = b, a % b

        return str1[:a]

sol = Solution()
print(sol.gcdOfStrings("ABCABC", "ABC"))   # ABC
print(sol.gcdOfStrings("ABABAB", "ABAB"))  # AB
print(sol.gcdOfStrings("LEET", "CODE"))    # "" (vacío)
