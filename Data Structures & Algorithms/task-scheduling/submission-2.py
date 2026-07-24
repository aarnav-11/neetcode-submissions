class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0]*26
        for task in tasks:
            freq[ord(task) - ord("A")] += 1

        freq = [count for count in freq if count > 0]
        heapq.heapify_max(freq)
        if len(freq) == 0:
            return 0

        q = deque()
        time = 0

        while freq or q:
            time += 1
            if freq:
                val = heapq.heappop_max(freq)
                val -= 1
                if val > 0:
                    q.append((val, time + n))

            if q and q[0][1] == time:
                val = q.popleft()[0]
                heapq.heappush_max(freq, val)
            
        return time


