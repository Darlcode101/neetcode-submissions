class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxHeap = [-s for s in stones]
        
        heapq.heapify(self.maxHeap)

        while len(self.maxHeap)>1:
            x =heapq.heappop(self.maxHeap)
            y = heapq.heappop(self.maxHeap)

            if x < y:
                heapq.heappush(self.maxHeap, x - y)
            
        if self.maxHeap:
            return abs(self.maxHeap[0])

        return 0



