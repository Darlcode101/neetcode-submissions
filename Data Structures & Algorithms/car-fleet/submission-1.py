class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = {}

        for i in range(len(position)):
            cars [position[i]]= (target- position[i])/speed[i]
        fleets = 0
        slowness = 0

        for j in sorted(cars.keys(),reverse = True):
            time = cars[j]

            if time>slowness:
                slowness = time 
                fleets += 1
        return fleets


    
