class Solution:
    def minimumSize(self,nums: List[int], maxOperations) -> int:
        left, right = 1, max(nums)

        while left < right:
            mid = (left + right) // 2
            operations = 0

            for num in nums:
                operations += (num - 1) // mid

            if operations > maxOperations:
                left = mid + 1
            else:
                right = mid

        return left
        