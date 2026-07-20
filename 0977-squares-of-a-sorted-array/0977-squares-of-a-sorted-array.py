class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        result = []
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        for i in range(len(neg)):
            neg[i] = neg[i] * neg[i]
        neg = neg[::-1]
        for i in range(len(pos)):
            pos[i] = pos[i] * pos[i]
        i = 0 
        j = 0
        while i < len(pos) and j < len(neg):
            if pos[i] < neg[j]:
                result.append(pos[i])
                i = i+1
            else:
                result.append(neg[j])
                j = j+1
        result.extend(pos[i:])
        result.extend(neg[j:])

        return result