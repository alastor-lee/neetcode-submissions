class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        prefixProds = [x for x in nums]
        suffixProds = [x for x in nums]
        for i in range(0, len(nums)):
            if i != 0:
                prefixProds[i] = prefixProds[i-1] * nums[i]
            else: prefixProds[i] = nums[i]
            j = len(nums) - 1 - i
            if j != len(nums) - 1:
                suffixProds[j] = suffixProds[j+1] * nums[j]
            else: suffixProds[j] = nums[j]
        print(prefixProds)
        print(suffixProds)
        res = []
        for i in range(0, len(nums)):
            if i == 0:
                res.append(suffixProds[i+1])
            elif i == len(nums) - 1:
                res.append(prefixProds[i-1])
            else:
                res.append(prefixProds[i-1] * suffixProds[i+1])
        print(res)
        return res 