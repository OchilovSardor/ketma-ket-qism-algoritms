def isAnagram(s, t):  # The function that have two parameters for comparison
    if len(s) != len(t): # If the length of two parameters are not equal 
        return False  #they are not anagram
    
    countS, countT = {}, {}   #I created two dictionaries for comparison

    for i in range(len(s)): #loop through the (index) of the s parametre
        countS[s[i]] = 1 + countS.get(s[i], 0) #Take the current letter from each word s[i] and
        countT[t[i]] = 1 + countT.get(t[i], 0) #t[i] check how many times it has appeared so far
    # in the dictionary, and increase that cout by 1,If the letter is not in the dictionary yet
    #start it count at 1.
    for c in countS: # Loop through all key elements of the dictionary
        if countS[c] != countT.get(c, 0): # if the number of same letters in two dicts are
            return False # not equal it is not anagram
    return True #but if they are equal they are anagram
    

print(isAnagram("sardor", "bardor"))
print(isAnagram("adam", "dama"))