

def hasDuplicate(nums):
    hashset = set() # I create new set for comparing
      
    for num in nums:     #loop through every element in the nums
        if num in hashset:  # if the element inside of our set 
            return True # it means this is duplicate
        else:  # if element not in the set
            hashset.add(num) # add this element to the set and loop again
    return False # when there is no duplicates retucn false
print(hasDuplicate([1, 3, 5, 2]))
