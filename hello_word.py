#greeting
#Two sum
class Solution:
  def twoSum(self, nums, target):
      hashmap = {}
      for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
      return []
 
solution = Solution()

test_case_1 = [2, 7, 11, 15]
target_1 = 9
result_1 = solution.twoSum(test_case_1, target_1)
print(f"Test case result: {result_1}")
