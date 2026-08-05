class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [x for x in nums]
        total = 0
        hasZero = False
        hasTwoOrMoreZeroes = False
        for num in nums:
            if num != 0:
                if total == 0:
                    total = 1 * num
                else:
                    total = total * num
            else: 
                if hasZero == True:
                    hasTwoOrMoreZeroes = True
                else: hasZero = True
        for i in range(0, len(nums)):
            if products[i] == 0:
                if hasTwoOrMoreZeroes:
                    products[i] = 0
                else: products[i] = total
            else:
                if hasZero:
                    products[i] = 0
                else:
                    products[i] = math.floor(total / products[i])
        return products