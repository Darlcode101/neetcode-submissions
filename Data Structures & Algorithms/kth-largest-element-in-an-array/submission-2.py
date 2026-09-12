class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-s for s in nums]
        heapq.heapify(nums)
        prev = 99999

        while k > 1:
            x = heapq.heappop(nums)
            y = prev
            
            if x != y:
                k -= 1
        
        return (nums[0]* -1)