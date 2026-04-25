class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7
        def gcd(a,b):
            while b:
                a , b = b , a % b
            return a
        lcm = (a*b) / gcd(a,b)
        low = min(a,b)
        high = n*(min(a,b))
        ans = high
        while low <= high :
            mid = low + (high - low)//2 
            count = (mid//a) + (mid//b) - (mid//lcm)
            if count >= n:
                ans = mid
                high = mid - 1
            else: 
                low = mid + 1
        return (ans) % MOD