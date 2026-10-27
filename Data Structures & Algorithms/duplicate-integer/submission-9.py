class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        current = 0
        prev = 0
        print(len(nums))

        for i in range(len(nums) -1 ):
            current = nums[i + 1]
            prev = nums[i]
            
            print("prev",prev)
            print("current",current)

            if current == prev:
                return True
        return False
                



