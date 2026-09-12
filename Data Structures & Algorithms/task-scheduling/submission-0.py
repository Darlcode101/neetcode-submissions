class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxHeap = [-s for s in count.values()]
        
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1

            # run a task from heap
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)


            # put it into cooldown if copies remain
                if cnt:
                    q.append([cnt, time + n  ])

            # check if a cooled-down task is ready
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time


