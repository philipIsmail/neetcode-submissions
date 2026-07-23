class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        frequency = [[] for i in range(len(nums) + 1)]

        for num, cnt in count.items():

            frequency[cnt].append(num)

        res = []
        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                res.append(num)
                if len(res) == k:
                    return res