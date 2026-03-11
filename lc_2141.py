
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 0, sum(batteries) // n
        
        while left <= right:
            mid = (left + right) // 2
            
            power = sum(min(b, mid) for b in batteries)
            
            if power >= mid * n:
                left = mid + 1
            else:
                right = mid - 1
                
        return right