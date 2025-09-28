#def look_for_key(main_box):
    #pile = main_box.make_a_pile_to_look_through()
    #while pile is not empty:
        #box = pile.grap_a_box()
        #for item in box:
         #   if item.is_a_box():
          #      pile.append(item)
           # elif item.is_a_key():
            #    print("I found the key")



# def sum(number):
#     result = 0
#     for i in range(number + 1):
#         result += i
#     return result 
#     #print(result)


# print(sum(5))

 
# def countdown(i):
#     print(i)
#     if i == 0:
#         return
#     else:
#        countdown(i - 1)


# print(countdown(100))


# s = ['s','a','r','d','o','r']
# def reverseString(s: list) -> list:
# 	a = 0
# 	b = len(s) - 1

# 	for _ in range(len(s) - 1):
# 		s[a], s[b] = s[b], s[a]
		
# 		a += 1
# 		b -= 1
# 	return s
# print(reverseString(s))


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
    