class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rev = {}
        for num in nums:
            rev[num] = rev.get(num, 0) + 1
        revs = sorted(rev.items(), key=lambda x: x[1], reverse = True)
        fin = []
        for pair in revs[:k]:
            fin.append(pair[0])
        return fin



        