nums = [3,2,4]
target = 6

def twoSum(nums, target):
        nums_with_index = [(num, i) for i, num in enumerate(nums)]
        nums_with_index.sort()  

        left = 0
        right = len(nums_with_index) - 1

        while right > left:
            left_val, left_idx = nums_with_index[left]
            right_val, right_idx = nums_with_index[right]

            our_sum = left_val + right_val
            if our_sum == target:
                return left_idx, right_idx
            elif our_sum > target:
                right -= 1  
            else:
                left += 1  




print(twoSum(nums,target))
