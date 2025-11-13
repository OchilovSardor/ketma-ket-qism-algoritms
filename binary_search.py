def binary_search(list, item): # our function takes two arameters first list which  we will 
    # search through, secont the item that we need to find
    low = 0   # index of the first item in the list 
    high = len(list) - 1 # index of the  last item in the list

    while low <= high: # the loop will run as long as the first value smaller than last 
        mid = (low + high) // 2 # I figure out the middle of the list, by it's index
        guess = list[mid] # the guess equal to the value thet located in the middle of the list
        if guess == item: # if our item equal to the middle value of the list
            return mid  # program found our item
        if guess > item: # if value of the middle index bigger than tiem that we need
            high = mid - 1 # index of the last value changed to the value before the middle value
        else: # in eny other cases (if middle value smaller than our item)
            low = mid + 1 # index of the first item changed to the item after the middle result
    return None # if the value of the first index smaller than last

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] # if our list not sorted it will cause None

print(binary_search(my_list, 5))
print(binary_search(my_list, -1))
print(binary_search(my_list, 45)) # we don't have these results in our list
