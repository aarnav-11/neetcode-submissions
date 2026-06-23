class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        prev = float("-inf")
        r_max = arr[-1]
        ans = [0] * len(arr)
        ans[-1] = -1

        for i in range(len(arr)-2, -1, -1):
            ans[i] = max(arr[i+1], ans[i+1])
            #track r_max, prev and make each element the max(r_max, prev)
        ans[-1] = -1
        return ans