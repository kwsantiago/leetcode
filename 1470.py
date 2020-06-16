class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        list1 = nums[:len(nums)//2]
        list2 = nums[len(nums)//2:]
        output = []
        for i in range(n):
            output.append(list1[i])
            output.append(list2[i])
        return output
