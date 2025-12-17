
nums = [1,2,4,6]

def product_of_array_except_self(nums):
    """Product of array except self"""

    res = [1] * (len(nums))  #create boxes which number equal to length of nums with value 1

    prefix = 1   # variable for containing prefix value of the nums
    for i in range(len(nums)): # Looping whrough the  nums
        res[i] = prefix  # i index of the box equal to the value of prefix
        prefix *= nums[i] # prefix equal to i value of nums multiplied to value of prefix
    postfix = 1  # variable for containing postfix value of nums
    for i in range(len(nums) - 1, -1, -1):  #Looping through nums but in reverse order
        res[i] *= postfix  # i value of the previous result equal to multiplication of postfix to i value
        postfix *= nums[i] # postfix value equal to multiplication of the i value of the nums to postfix
    return res


print(nums)
print(product_of_array_except_self(nums))