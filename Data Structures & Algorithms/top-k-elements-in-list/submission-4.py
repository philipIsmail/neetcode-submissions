class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        #populate our dict with count of each element(key)
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        #copy over to our freq bucket with count as 'key'
        for n, c in count.items():
            freq[c].append(n)

        res = []
        #get the result by iterating in descending order
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
        
        return res[:k]