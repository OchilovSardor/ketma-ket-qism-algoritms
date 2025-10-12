
def sortes(arr):
    if len(arr) < 2:     # base case 
        return arr        # if there only one element in the array it is already sorted
    else:                  # Inductive case
        pivot = arr[0]                 # we choose first elemeent of the array as a pivot
        smaller = [i for i in arr[1:] if i <= pivot]    # all numbers that smaller than our pivot
        # Notion: It is important that smaller number prossessing first
        bigger = [i for i in arr[1:] if i > pivot]      # all number that bigger than pivot
        
        return sortes(smaller) + [pivot] + sortes(bigger)    # we adding all our results to get sorted array


print(sortes([1, 5, 3, 7, 11, 4])) 



