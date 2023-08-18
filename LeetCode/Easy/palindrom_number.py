class Solution:
    
    def IsPalindrom(x: int) -> bool:
        if x < 0: return False
        elif x == 0: return True
        digits = [0 for _ in range(len(str(x)))]
        for i in range(len(str(x)) - 1, -1, -1):
            digits[i] = x % 10
            x //= 10
        for i in range(len(digits) // 2):
            if digits[i] != digits[-1 - i]: return False
        return True
