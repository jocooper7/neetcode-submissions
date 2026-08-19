class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        result = high

        while low <= high:
            mid = (low + high) // 2
            total = 0
            for ele in piles:
                total += -(-ele // mid)
            if total <= h:
                result = min(result, mid)
                high = mid - 1
            else:
                low = mid + 1
        return result