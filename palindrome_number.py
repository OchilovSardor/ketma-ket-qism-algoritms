
def isPalindrome(x):
    
    if x <= 0:      # If the given number negative 
        return False  
      #finding largest power of 10
    div = 1            # we will use this for finding leftmost digit
    while x >= 10 * div:  # This loop will run as long as,x bigger than devider multiplied by 10
        div *= 10    # then we multiply div by 10, because we need to find leftmost digit
    
    while x: # removing leftmost and rightmost digits
        right = x % 10     # right equal to rightmost digit,which is the reminder
        left = x // div     # left equal to leftmost digit,which is the number devided by div 

        if left != right:  # if leftmost and rightmost digits are not equal
            return False  # False because it means that they are not palindrome numbers
        # But if they are equal
        x = (x % div) // 10 # we remove leftmost and rightmost numbers,and prossess begins again, but only with remainig numbers
        div = div // 100 # we return div to it's original value which is 1
    return True    # if our while works until the end of digits it is True

print(isPalindrome(0))