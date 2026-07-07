class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #sort by position
        #map sorting to speed
        #calculate time taken and track using monotonic stack
        position = position[::-1]
        speed = speed[::-1]
        sorted_positions, sorted_speed = zip(*sorted(zip(position, speed)))
        sorted_positions, sorted_speed = list(sorted_positions), list(sorted_speed)
        stack = []
        time = [0] * len(position)

        for i, pos in enumerate(sorted_positions):
            time_single = (target - pos) / sorted_speed[i]
            time[i] = time_single
            while stack and time[stack[-1]] <= time_single:
                stack.pop()
            stack.append(i)
        return len(stack)