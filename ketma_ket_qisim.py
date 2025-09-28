

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

def isValidSubsequence(array, sequence):
    arr_ind = 0
    sec_ind = 0
    while arr_ind < len(array) and sec_ind < len(sequence):
        if array[arr_ind] == sequence[sec_ind]: 
            sec_ind += 1
        arr_ind += 1
    if sec_ind == len(sequence):
       return True
    else:
       return False

print(isValidSubsequence(array, sequence))
    
