
nums = [100,4,200,1,3,2]

def longest_C_S(nums):    

    numSet = set(nums) 
    longest = 0

    for n in numSet:
        if (n - 1) not in numSet:
            length = 1
            while (n + length) in numSet:
                length += 1 
            longest = max (length, longest)
    return longest

print(longest_C_S(nums))
