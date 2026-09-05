class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            k = max(piles)
            return k
        l, r = 1, max(piles)

        while l<=r:
            mid = (l+r)//2
            hours = 0
            for pile in piles:
                hours += (mid + pile -1)//mid
           
            if hours <= h :
                r = mid - 1
            else :
                l = mid + 1
        return l


            
        